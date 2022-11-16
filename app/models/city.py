from django.contrib.auth.models import models
from .state import State

class City(models.Model):
    name=models.CharField(max_length=30, null=False, blank=False)
    state=models.ForeignKey(State, on_delete=models.CASCADE, related_name='cities')

    def __str__(self):
        return self.name