import json
from django.db import models
from django.utils import timezone
from laboratory.models import Laboratory

from django.contrib.auth.models import User


class Attendance(models.Model):
    """出席情報
    """

    def create_attendance(self, laboratory, member_list):
        attendance = Attendance.objects.create(
            laboratory=laboratory,
            attendance_member=json.dumps(member_list)
        )

        attendance.save()
        return attendance

    def update_attendance(self, laboratory, member_list):
        attendance = Attendance.objects.get(date=timezone.now, laboratory=laboratory)
        attendance["attendance_member"] = json.dumps(member_list)
        
        attendance.save()
        return attendance

    def get_attendance_member(self, laboratory):
        attendance = Attendance.objects.get(date=timezone.now, laboratory=laboratory)
        return json.loads(attendance.attendance_member)

    date = models.DateField(verbose_name="日付", default=timezone.now)
    laboratory = models.ForeignKey(Laboratory, on_delete=models.CASCADE)
    attendance_member = models.JSONField(verbose_name="出席者")

    class Meta:
        verbose_name = verbose_name_plural = "出席情報"

    def __str__(self):
        attendance_member_num = len(json.loads(self.attendance_member))
        return f"{self.date}: {self.laboratory}, 出席{attendance_member_num}人"
    

class SeatPosition(models.Model):
    attendance = models.ForeignKey(Attendance, on_delete=models.CASCADE)
    seat_id = models.IntegerField(verbose_name="座席ID")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = verbose_name_plural = "座席情報"

    def __str__(self):
        return f"{self.attendance.date}: {self.seat_id}（{self.seat_id}）"
