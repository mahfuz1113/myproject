from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from .models import TimesheetDetail
# Create your views here.
class TimesheetListView(ListView):
    model = TimesheetDetail

class TimesheetDetailView(DetailView):
    model = TimesheetDetail
