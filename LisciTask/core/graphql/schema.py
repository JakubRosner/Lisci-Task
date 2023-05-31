import graphene
from . import queries, mutations


class Query(
    queries.LearningActivityQuery,
    queries.UserDataQuery,
    queries.CourseQuery,
    queries.UserQuery,
):
    pass


class Mutation(graphene.ObjectType):
    # CourseType
    create_course_type = mutations.CreateCourseMutation.Field()
    update_course_type = mutations.UpdateCourseMutation.Field()
    delete_course_type = mutations.DeleteCourseMutation.Field()

    # LearningActivityType
    create_learning_activity_type = mutations.CreateLearningActivityMutation.Field()
    update_learning_activity_type = mutations.UpdateLearningActivityMutation.Field()
    delete_learning_activity_type = mutations.DeleteLearningActivityMutation.Field()

    # UserDataType
    create_user_data_type = mutations.CreateUserDataMutation.Field()
    update_user_data_type = mutations.UpdateUserDataMutation.Field()
    delete_user_data_type = mutations.DeleteUserDataMutation.Field()

    # UserDataType
    create_user_type = mutations.CreateUserMutation.Field()
    update_user_type = mutations.UpdateUserMutation.Field()
    delete_user_type = mutations.DeleteUserMutation.Field()
