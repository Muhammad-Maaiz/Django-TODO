from django.contrib import admin
from taskcrud.models import Task

# Register your models here.
class AdminTask(admin.ModelAdmin):
    list_display = ('user','task_title','task_description','task_due_date','task_created_at','task_updated_at')

admin.site.register(Task, AdminTask)