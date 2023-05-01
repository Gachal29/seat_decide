from django.contrib import admin
from django.urls import path

from attendance import views as attendance_views
from laboratory import views as laboratory_views
from .login_sets import Login
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', Login.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('', laboratory_views.TopView.as_view(), name="top"),
    path('seat_confirmation/', attendance_views.SeatConfirmationView.as_view(), name="seat_confirm"),
    path('seat_decide/', laboratory_views.SeatDecideView.as_view(), name="seat-decide"),
]
