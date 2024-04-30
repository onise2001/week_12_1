from django.shortcuts import render
from .models import Event

# Create your views here.

def index(request):

    if request.method == "POST":
        search = request.POST.get('search')
        events = Event.objects.filter(title__contains=search)
        context = {
            "events": events
        }
        return render(request, "planner/index.html", context)


    events = Event.objects.all()
    context = {
        "events": events
    }
    return render(request, "planner/index.html", context)


def add(request):

    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        date = request.POST.get("date")
        location = request.POST.get("location")
        event = Event(title=title,descritpion=description, date=date, location=location)
        event.save()


    return render(request, "planner/add_event.html")