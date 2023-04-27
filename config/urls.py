from django.contrib import admin
from django.urls import path

from attendance import views as attendance_views
from laboratory import views as laboratory_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', laboratory_views.TopView.as_view(), name="top"),
]
