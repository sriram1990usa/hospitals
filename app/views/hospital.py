from django.shortcuts import render
from app.models.state import State
from app.models.city import City
from app.models.hospital import Hospital
from app.models.facility import Facility
from app.models.availability import Availability

def hospitalview(request):
    states=State.objects.all()
    cities=City.objects.all()
    hospitals=Hospital.objects.all()
    facilities = Facility.objects.all().order_by('pk')

    
    selected_state_id=request.GET.get('state')  
    if selected_state_id:
        cities=cities.filter(state=selected_state_id)
    else:
        cities=City.objects.all()
    
    selected_city_id=request.GET.get('city') 
    if selected_city_id:        
        hospitals=hospitals.filter(city=City(pk=selected_city_id))
       
    selected_facility_id=request.GET.get('facility')
    if selected_facility_id:
        availabilities=Availability.objects.all()
        
        if selected_city_id:
            availabilities=availabilities.filter(
            hospital__city=City(pk=selected_city_id))
        
        availabilities=availabilities.filter(
            facility=Facility(pk=selected_facility_id),
            available__gt=0)
       
        hospitals=[]
        for avl in availabilities:
            hospitals.append(avl.hospital)
    
    context={
        'facilities':facilities,
        'cities':cities,
        'states':states,
        'hospitals':hospitals,
        'selected_state_id':selected_state_id,
        'selected_city_id':selected_city_id,
        'selected_facility_id':selected_facility_id
    }
   
    return render(request,'facility.html', context)
