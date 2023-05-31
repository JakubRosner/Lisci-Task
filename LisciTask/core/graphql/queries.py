import graphene
from . import types, connections


class UserQuery(graphene.ObjectType):
    user = graphene.Node.Field(types.UserType)
    all_users = graphene.relay.ConnectionField(connections.UserConnection)


class CourseQuery(graphene.ObjectType):
    course = graphene.Node.Field(types.CourseType)
    all_courses = graphene.relay.ConnectionField(connections.CourseConnection)


class LearningActivityQuery(graphene.ObjectType):
    learning_activity = graphene.Node.Field(types.LearningActivityType)
    all_learning_activities = graphene.relay.ConnectionField(connections.LearningActivityConnection)


class UserDataQuery(graphene.ObjectType):
    user_data = graphene.Node.Field(types.UserDataType)
    all_user_datas = graphene.relay.ConnectionField(connections.UserDataConnection)
