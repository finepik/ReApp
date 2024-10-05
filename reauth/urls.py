from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import ReObtainTokenPairView, RegisterView, LogoutView, DoctorProfileAPIView, PatientProfileAPIView, \
    DoctorProfileDetailAPIView, PatientProfileDetailAPIView, DiagnosisAPIView, RoleAPIView

app_name = 'reauth'
urlpatterns = [
    path('login/', ReObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('logout/', LogoutView.as_view(), name='auth_logout'),
    path('doctor_profile/', DoctorProfileAPIView.as_view(), name='doctor-profile'),
    path('doctor_profile/<int:pk>/', DoctorProfileDetailAPIView.as_view(), name='doctor-profile-detail'),
    path('patient_profile/', PatientProfileAPIView.as_view(), name='patient-profile'),
    path('patient_profile/<int:pk>/', PatientProfileDetailAPIView.as_view(), name='patient-profile-detail'),
    path('diagnoses/', DiagnosisAPIView.as_view(), name='diagnoses'),
    path('role/', RoleAPIView.as_view(), name='role'),
    ]