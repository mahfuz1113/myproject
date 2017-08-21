from django.contrib import admin
from .models import Project, TimesheetDetail, Workcode
# Register your models here.
admin.site.register(Project)
admin.site.register(TimesheetDetail)
admin.site.register(Workcode)
