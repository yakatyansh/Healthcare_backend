from rest_framework import viewsets
from .models import Patient
from .serializers import PatientSerializer
from rest_framework.permissions import IsAuthenticated

class PatientViewSet(viewsets.ModelViewSet):

    queryset = Patient.objects.all()

    serializer_class = PatientSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):

        return Patient.objects.filter(user=self.request.user)

    def perform_create(self, serializer):

        serializer.save(user=self.request.user)