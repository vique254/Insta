from django.http  import HttpResponse
from django.shortcuts import render
import datetime as dt
# Create your views here.
def home(request):
    return render(request,'home.html')

def convert_dates(dates):

    # Function that gets the weekday number for the date.
    day_number = dt.date.weekday(dates)

    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday',"Sunday"]

    # Returning the actual day of the week
    day = days[day_number]
    return day