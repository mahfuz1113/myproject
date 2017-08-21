from django.conf.urls import url
from .views import TimesheetListView, TimesheetDetailView

app_name = 'timesheet'

urlpatterns = [
    url('^$', TimesheetListView.as_view(), name='timesheetlist'),
    url('^timesheet/',TimesheetDetailView.as_view(), name='timesheetdetail')
]
