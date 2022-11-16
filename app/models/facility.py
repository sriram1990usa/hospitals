from django.contrib.auth.models import models
from .hospital import Hospital

class Facility(models.Model):
    title= models.CharField(max_length=30, null=False, blank=False, default='')
   
    def __str__(self):
        return self.title

    '''
    hospital=models.OneToOneField(Hospital, on_delete=models.CASCADE, primary_key=True)
    oxygen_beds_total=models.IntegerField(default=0)
    oxygen_beds_available=models.IntegerField(default=0)
    oxygen_cylinder_total=models.IntegerField(default=0)
    oxygen_cylinder_available=models.IntegerField(default=0)
    ventilator_total=models.IntegerField(default=0)
    ventilator_available=models.IntegerField(default=0)
    def __str__(self):
        return self.hospital.name

    '''
   
  
   