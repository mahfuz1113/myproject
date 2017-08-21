from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Workcode(models.Model):
    workcode = models.PositiveSmallIntegerField()

    def __str__(self):
        return str(self.workcode)


class Project(models.Model):
    project = models.CharField(max_length=10)

    def __str__(self):
        return self.project


class TimesheetDetail(models.Model):
    user = models.ForeignKey(User)
    workdate = models.DateField()
    workcode = models.ForeignKey(Workcode)
    project = models.ForeignKey(Project)
    hours = models.PositiveSmallIntegerField()

    def __str__(self):
        return ('{} // {} // {}H').format(self.user.username,self.workdate,self.hours)
