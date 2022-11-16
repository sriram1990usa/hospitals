from django.shortcuts import render
from app.models.state import State
from app.models.city import City
from app.models.hospital import Hospital
from app.models.facility import Facility
from app.models.availability import Availability
from django.views import generic


class HospitalDetailView(generic.DetailView):
    model=Hospital
    
'''
def hospitalDetailView(request, id):
    print('in hospitalDetailView.py')
    error_message=f"no errors, id is: {id}"
    print('ln 16 error_message: ', error_message)
    print('ln 17 type of id: ', type(id))
    hospitals=Hospital.objects.all()
    print('ln 19 hospitals: ', hospitals)
    hospital=hospitals.filter(pk=id)
    print('ln 21 hospital: ', hospital) #<Queryset[<Hospital:hosp1c1s1>]
    context={
        'error_message':error_message,
        'hospital':hospital  
    }
    return render(request, 'hospital_detail.html', context=context)
'''