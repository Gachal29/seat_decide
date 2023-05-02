from typing import Any, Dict
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from laboratory.models import Laboratory, AffiliationLab


class TopView(LoginRequiredMixin, TemplateView):
    template_name = "top.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context["user"] = user
        try:
            context["laboratory"] = Laboratory.objects.get(admin_user=user)
        except:
            pass

        return context


class SeatDecideView(LoginRequiredMixin, TemplateView):
    template_name = "seat_decide.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)

        user = self.request.user

        laboratory = Laboratory.objects.get(admin_user=user)
        members = AffiliationLab.objects.filter(laboratory=laboratory).exclude(isTeacher=True)

        members_3th = []
        members_4th = []
        for member in members:
            if member.user.email[1:3] == "21":
                members_3th.append(member)
            elif member.user.email[1:3] == "20":
                members_4th.append(member)

        context["members_3th"] = members_3th
        context["members_4th"] = members_4th

        print(members_4th)

        return context
