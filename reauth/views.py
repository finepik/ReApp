from django.contrib.auth.models import User
from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import DoctorProfile, PatientProfile, Diagnosis
from .serializers import ReTokenObtainPairSerializer, RegisterSerializer, DoctorProfileSerializer, \
    PatientProfileSerializer, DiagnosisSerializer


class ReObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = ReTokenObtainPairSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class DoctorProfileAPIView(APIView):
    def get(self, request):
        doctor_profile = DoctorProfile.objects.all()
        return Response({"data": DoctorProfileSerializer(doctor_profile, many=True).data})

    def post(self, request):
        serializer = DoctorProfileSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"data": serializer.data})


class DoctorProfileDetailAPIView(APIView):
    def get(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method GET not allowed"})

        try:
            doctor_profile = DoctorProfile.objects.get(pk=pk)
        except:
            return Response({"error": "Method GET not allowed"})

        return Response({"data": DoctorProfileSerializer(doctor_profile).data})

    def patch(self, request, *args, **kwargs):
        id_doctor = kwargs.get("pk", None)

        if not id_doctor:
            return Response({"error": "Method PUT not allowed, not id_template"})

        try:
            instance = DoctorProfile.objects.get(pk=id_doctor)
        except:
            return Response({"error": "Method PUT not allowed"})

        updated_profile = DoctorProfileSerializer().update(validated_data=request.data, instance=instance)
        return Response({"data": DoctorProfileSerializer(updated_profile).data})


class PatientProfileAPIView(APIView):
    def get(self, request):
        patient_profile = PatientProfile.objects.all()
        return Response({"data": PatientProfileSerializer(patient_profile, many=True).data})

    def post(self, request):
        serializer = PatientProfileSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"data": serializer.data})


class PatientProfileDetailAPIView(APIView):
    def get(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method GET not allowed"})

        try:
            patient_profile = PatientProfile.objects.get(pk=pk)
        except:
            return Response({"error": "Method GET not allowed"})

        return Response({"data": PatientProfileSerializer(patient_profile).data})

    def patch(self, request, *args, **kwargs):
        id_patient = kwargs.get("pk", None)
        if not id_patient:
            return Response({"error": "Method PUT not allowed, not id_template"})

        try:
            instance = PatientProfile.objects.get(pk=id_patient)
        except:
            return Response({"error": "Method PUT not allowed"})

        updated_profile = PatientProfileSerializer().update(validated_data=request.data, instance=instance)
        return Response({"data": PatientProfileSerializer(updated_profile).data})


class DiagnosisAPIView(APIView):
    def get(self, request):
        diagnosis = Diagnosis.objects.all()
        return Response({"data": DiagnosisSerializer(diagnosis, many=True).data})


class RoleAPIView(APIView):
    def get(self, request):
        is_doctor = False
        if DoctorProfile.objects.get(user=request.user.id):
            is_doctor = True
        return Response({"data": {"is_doctor": is_doctor}})
