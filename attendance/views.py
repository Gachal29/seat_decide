from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from attendance.models import Attendance, SeatPosition
from laboratory.models import AffiliationLab


class SeatConfirmationView(LoginRequiredMixin, TemplateView):
    template_name = "seat_confirmation.html"

    def get_context_data(self, **kwargs: any) -> dict[str, any]:
        context = super().get_context_data(**kwargs)
        
        user = self.request.user
        today = timezone.now()

        affiliation_lab = AffiliationLab.objects.get(user=user)
        attendance = Attendance.objects.get(date=today, laboratory=affiliation_lab.laboratory)
        seat_position = SeatPosition.objects.get(user=user, attendance=attendance)
        
        context["seat_id"] = seat_position.seat_id

        return context
