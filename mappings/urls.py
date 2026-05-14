from rest_framework.routers import DefaultRouter
from .views import  PatientDoctorMappingViewSet

router = DefaultRouter()

router.register(r'mappings', PatientDoctorMappingViewSet)

urlpatterns = router.urls