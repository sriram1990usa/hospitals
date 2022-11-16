from django.contrib.auth.models import models
from .city import City
from .hospital import Hospital
from .facility import Facility

class Availability(models.Model):
    hospital=models.ForeignKey(Hospital, on_delete=models.CASCADE, related_name='availabilities')
    facility=models.ForeignKey(Facility, on_delete=models.CASCADE, related_name='availabilities')
    total=models.IntegerField(default=0)
    available=models.IntegerField(default=0)
    updated_at=models.DateTimeField(auto_now=True)
   
   
    def __str__(self):
        return f'{self.hospital.name} - {self.facility.title}'