from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import PatientDoctorMapping
from .serializers import PatientDoctorMappingSerializer


class PatientDoctorMappingViewSet(viewsets.ModelViewSet):

    queryset = PatientDoctorMapping.objects.all()

    serializer_class = PatientDoctorMappingSerializer

    permission_classes = [IsAuthenticated]


    @action(detail=False, methods=['get'], url_path=r'patient/(?P<patient_id>\d+)')
    def get_patient_doctors(self, request, patient_id=None):

        mappings = PatientDoctorMapping.objects.filter(
            patient_id=patient_id
        )

        serializer = self.get_serializer(mappings, many=True)

        return Response(serializer.data)