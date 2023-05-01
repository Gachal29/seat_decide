from typing import Any, Dict
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from laboratory.models import Laboratory


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
