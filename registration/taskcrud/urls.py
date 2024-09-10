from django.urls import path
from taskcrud import views

urlpatterns = [
    path('addtask/', views.add_task, name='addtask'),
    path('updatetask/<int:id>', views.update_task, name='updatetask'),
    path('viewtask/', views.view_task, name='viewtask'),
    path('deletetask/<int:id>', views.delete_task, name='deletetask'),
]
