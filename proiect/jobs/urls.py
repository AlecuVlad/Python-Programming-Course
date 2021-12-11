from django.urls import path

from jobs import views

app_name = 'jobs'

urlpatterns = [
    path('', views.CreateJobView.as_view(), name='add'),
    path('list/', views.ListJobView.as_view(), name='list'),
    path('<int:pk>/update/', views.UpdateJobView.as_view(), name='modify'),
    path('delete/<int:pk>/', views.delete_job, name='delete'),
]
