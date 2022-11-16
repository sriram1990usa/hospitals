from django.contrib.auth.models import models
from .city import City

class Hospital(models.Model):
    name=models.CharField(max_length=30, null=False, blank=False)
    address=models.CharField(max_length=30, null=False, blank=False)
    phone=models.CharField(max_length=30, null=False, blank=False)
    city=models.ForeignKey(City, on_delete=models.CASCADE, related_name='hospitals')

    def __str__(self):
        return self.name