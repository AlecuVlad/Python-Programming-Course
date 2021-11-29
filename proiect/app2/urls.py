from django.urls import path
from app2 import views

app_name = 'app2'
urlpatterns = [
    path('new_timesheet', views.newPontaj, name='pontaj'),
    path('stop_timesheet', views.stopTimesheet, name='oprire_pontaj'),
]
