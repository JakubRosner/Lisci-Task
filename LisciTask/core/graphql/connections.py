import graphene

from . import types


class UserConnection(graphene.relay.Connection):
    class Meta:
        node = types.UserType


class UserDataConnection(graphene.relay.Connection):
    class Meta:
        node = types.UserDataType


class CourseConnection(graphene.relay.Connection):
    class Meta:
        node = types.CourseType


class LearningActivityConnection(graphene.relay.Connection):
    class Meta:
        node = types.LearningActivityType
