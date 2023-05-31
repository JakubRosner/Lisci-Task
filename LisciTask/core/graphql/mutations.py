import graphene
from .. import utils
from .. import models
from . import types
from django.contrib.auth.models import User



# Course CRUD
class CreateCourseMutation(utils.GetOrCreateMutation):
    model = models.Course
    obj = graphene.Field(types.CourseType)

    class Arguments:
        name = graphene.String(required=True)


class UpdateCourseMutation(utils.UpdateMutation):
    model = models.Course
    obj = graphene.Field(types.CourseType)

    class Arguments:
        id = graphene.ID(required=True)
        name = graphene.String()


class DeleteCourseMutation(utils.DeleteMutation):
    model = models.Course
    obj = graphene.Field(types.CourseType)

    class Arguments:
        id = graphene.ID(required=True)


# LearningActivity CRUD
class CreateLearningActivityMutation(utils.GetOrCreateMutation):
    model = models.LearningActivity
    obj = graphene.Field(types.LearningActivityType)

    class Arguments:
        name = graphene.String(required=True)
        completed = graphene.Boolean()
        course_id = graphene.ID()


class UpdateLearningActivityMutation(utils.UpdateMutation):
    model = models.LearningActivity
    obj = graphene.Field(types.LearningActivityType)

    class Arguments:
        id = graphene.ID(required=True)
        name = graphene.String(required=True)
        completed = graphene.Boolean()
        course_id = graphene.ID()


class DeleteLearningActivityMutation(utils.DeleteMutation):
    model = models.LearningActivity
    obj = graphene.Field(types.LearningActivityType)

    class Arguments:
        id = graphene.ID(required=True)


# UserData CRUD
class CreateUserDataMutation(utils.GetOrCreateMutation):
    model = models.UserData
    obj = graphene.Field(types.UserDataType)

    class Arguments:
        timestamp = graphene.DateTime()
        user_id = graphene.ID(required=True)
        learning_activity_id = graphene.ID()
        data = graphene.String()
        status = utils.Enums.STATUS()
        completed_at = graphene.DateTime()
        progress = graphene.Float()
        score = graphene.Float()
        manually_finished = graphene.Boolean()
        manually_finished_at = graphene.Boolean()


class UpdateUserDataMutation(utils.UpdateMutation):
    model = models.UserData
    obj = graphene.Field(types.UserDataType)

    class Arguments:
        id = graphene.ID(required=True)
        timestamp = graphene.DateTime()
        user_id = graphene.ID(required=True)
        learning_activity_id = graphene.ID()
        data = graphene.String()
        status = utils.Enums.STATUS()
        completed_at = graphene.DateTime()
        progress = graphene.Float()
        score = graphene.Float()
        manually_finished = graphene.Boolean()
        manually_finished_at = graphene.Boolean()


class DeleteUserDataMutation(utils.DeleteMutation):
    model = models.UserData
    obj = graphene.Field(types.UserDataType)

    class Arguments:
        id = graphene.ID(required=True)


# User CRUD
class CreateUserMutation(utils.GetOrCreateMutation):
    model = User
    obj = graphene.Field(types.UserType)

    class Arguments:
        username = graphene.String(required=True)
        first_name = graphene.String()
        last_name = graphene.String()
        # create field validation for email
        email = graphene.String()


class UpdateUserMutation(utils.UpdateMutation):
    model = User
    obj = graphene.Field(types.UserType)

    class Arguments:
        id = graphene.ID(required=True)
        username = graphene.String(required=True)
        first_name = graphene.String()
        last_name = graphene.String()
        # create field validation for email
        email = graphene.String()


class DeleteUserMutation(utils.DeleteMutation):
    model = User
    obj = graphene.Field(types.UserType)

    class Arguments:
        id = graphene.ID(required=True)
