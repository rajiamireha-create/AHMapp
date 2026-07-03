from django.urls import path
from ahmadapp import views


urlpatterns = [
    
    path('complete/<task_id>/',views.completed_task, name='complete'),
    path('',views.ahmadapp, name='ahmadapp'),
    path('edit/<task_id>/',views.edit_task, name='edit'),
    path('delete/<task_id>/',views.delete_task, name='delete'),
    path('pending/<task_id>/',views.pending_task, name='pending'), 
]
