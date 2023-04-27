from django.db import models
from django.contrib.auth.models import User


class Laboratory(models.Model):
    """研究室
    """

    def create_lab(self, user, name):
        if (not user.email[user.email.find("@"):] == "@do-johodai.ac.jp"):
            raise ValueError("学生は研究室を作成できません。")
        
        lab = Laboratory.objects.create(name=name, admin_user=user)
        lab.save()
        return lab

    name = models.CharField(
        verbose_name="研究室名",
        max_length=100,
    )

    admin_user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = verbose_name_plural = "研究室"

    def __str__(self):
        return self.name
    

class AffiliationLab(models.Model):
    """所属研究室
    """

    def create_affiliation_lab(self, laboratory, user):
        affiliation_lab = AffiliationLab.objects.create(laboratory=laboratory, user=user)

        if (user.email[user.email.find("@"):] == "@do-johodai.ac.jp"):
            affiliation_lab["isTeacher"] = True

        affiliation_lab.save()
        return affiliation_lab
        

    laboratory = models.ForeignKey(Laboratory, on_delete=models.CASCADE)
    
    isTeacher = models.BooleanField(verbose_name="教員", default=False)
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = verbose_name_plural = "所属研究室"

    def __str__(self):
        return f"{self.laboratory}: {self.user.get_full_name()}"
