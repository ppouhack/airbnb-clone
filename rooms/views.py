from django.shortcuts import render
from . import models

# from django.http import HttpResponse


def all_rooms(request):
    # now = datetime.now()
    # hungry = True
    # return HttpResponse(context="hello")

    all_rooms = models.Room.objects.all()
    return render(request, "rooms/home.html", context={"rooms": all_rooms})
