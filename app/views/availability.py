from django.shortcuts import render
from app.models.facility import Facility
from app.models.state import State
from app.models.city import City
from app.models.availability import Availability

def availability(request):
    facilities = Facility.objects.all().order_by('title')
    cities=City.objects.all()
    states=State.objects.all()
    availabilities=Availability.objects.all()
    print('ln 12 availabilities', availabilities)

    context={
        'facilities':facilities,
        'cities':cities,
        'states':states,
        'availabilities':availabilities
    }
   
    return render(request,'facility.html', context)
