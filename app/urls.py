from django.urls import path
from app.views.home import home
from app.views.facility import facility
from app.views.hospitalDetailView import HospitalDetailView

urlpatterns = [
    path('', home, name='home'),
    path('facility/', facility),
    path('hospital/<int:pk>/',HospitalDetailView.as_view(), name='hospital_detail')
]
