from django.contrib.auth.models import User
from rest_framework import permissions, viewsets

from . import models, serializers


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = [permissions.AllowAny]


class UserDataViewSet(viewsets.ModelViewSet):
    queryset = models.UserData.objects.all()
    serializer_class = serializers.UserDataSerializer
    permission_classes = [permissions.AllowAny]


class LearningActivityViewSet(viewsets.ModelViewSet):
    queryset = models.LearningActivity.objects.all()
    serializer_class = serializers.LearningActivitySerializer
    permission_classes = [permissions.AllowAny]


class CourseViewSet(viewsets.ModelViewSet):
    queryset = models.Course.objects.all()
    serializer_class = serializers.CourseSerializer
    permission_classes = [permissions.AllowAny]
