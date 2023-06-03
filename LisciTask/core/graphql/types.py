import graphene
from django.contrib.auth.models import User
from graphene_django import DjangoObjectType

from .. import models


class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = "__all__"
        interfaces = (graphene.relay.Node,)


class CourseType(DjangoObjectType):
    class Meta:
        model = models.Course
        fields = "__all__"
        interfaces = (graphene.relay.Node,)


class LearningActivityType(DjangoObjectType):
    class Meta:
        model = models.LearningActivity
        fields = "__all__"
        interfaces = (graphene.relay.Node,)


class UserDataType(DjangoObjectType):
    class Meta:
        model = models.UserData
        fields = "__all__"
        interfaces = (graphene.relay.Node,)
