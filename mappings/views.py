from rest_framework import viewsets
from .models import PatientDoctorMapping as Mappings
from .serializers import PatientDoctorMappingSerializer

class MappingViewSet(viewsets.ModelViewSet):

    queryset = Mappings.objects.all()

    serializer_class = PatientDoctorMappingSerializer