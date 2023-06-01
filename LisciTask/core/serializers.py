from rest_framework import serializers
from . import models
from django.contrib.auth.models import User


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Course
        fields = ["name",]


class LearningActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.LearningActivity
        fields = ["name", "completed", "course"]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email"]


class UserDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserData
        fields = [
            "user",
            "learning_activity",
            "data",
            "status",
            "completed_at",
            "progress",
            "score",
            "manually_finished",
            "manually_finished_at"
        ]
