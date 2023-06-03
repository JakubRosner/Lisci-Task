import graphene
from graphene_django import DjangoObjectType
from .. import models
from django.contrib.auth.models import User


class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = "__all__"
        interfaces = (graphene.relay.Node,)


class CourseType(DjangoObjectType):
    class Meta:
        model = models.Course
        fields = "__all__"
        interfaces = (graphene.relay.Node, )


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
