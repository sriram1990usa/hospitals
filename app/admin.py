from django.contrib import admin
from app.models.state import State
from app.models.city import City
from app.models.hospital import Hospital
from app.models.facility import Facility
from app.models.availability import Availability
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=Hospital)
def afterHospitalSave(signal, instance, **kwargs):
    facilities = Facility.objects.all()
    for facility in facilities:
        availability=Availability(hospital=instance, facility=facility)
        availability.save()

@receiver(post_save, sender=Facility)
def afterFacilitySave(signal, instance, **kwargs):
    hospitals = Hospital.objects.all()
    for hospital in hospitals:
        availability=Availability(hospital=hospital, facility=instance)
        availability.save() 

'''
  print("Save Services For ", instance.name, instance.phone)
    service=Service(hospital=instance)
    service.save() 
'''
class StateAdmin(admin.ModelAdmin):
    model=State
    list_display=['name']

class CityAdmin(admin.ModelAdmin):
    model=City
    list_display=['name', 'state']

class HospitalAdmin(admin.ModelAdmin):
    model=Hospital
    list_display=['name', 'phone', 'address', 'city']

class FacilityAdmin(admin.ModelAdmin):
    model=Facility
    list_display=['title']      

class AvailabilityAdmin(admin.ModelAdmin):
    model=Availability
    list_display=['hospital', 'facility', 'total', 'available', 'updated_at']
    list_editable=['total', 'available']

    '''
class ServiceAdmin(admin.ModelAdmin):
    model=Service
    list_display=['service']   
  
    list_display=['hospital', 
                  'oxygen_beds',               
                  'oxygen_cylinder',                 
                  'ventilator' ]
    
    def oxygen_beds(self, object):
        return f'{object.oxygen_beds_available}/{object.oxygen_beds_total}'

    def oxygen_cylinder(self, object):
        return f'{object.oxygen_cylinder_available}/{object.oxygen_cylinder_total}'

    def ventilator(self, object):
         return f'{object.ventilator_available}/{object.ventilator_total}'
    '''
# Register your models here.
admin.site.register(State, StateAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Hospital, HospitalAdmin)
admin.site.register(Facility, FacilityAdmin)
admin.site.register(Availability, AvailabilityAdmin)