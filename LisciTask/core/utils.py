import graphene
from enum import auto
from django.db import models
from graphql.error import GraphQLError


class STATUS(models.TextChoices):
    COMPLETED = auto()
    NOT_COMPLETED = auto()


class Enums:
    STATUS = graphene.Enum.from_enum(STATUS)


def exists_or_raise(model, id):
    try:
        return model.objects.get(id=id)
    except model.DoesNotExist:
        raise GraphQLError("Objects does not exists")

class GetOrCreateMutation(graphene.Mutation):
    created = graphene.Boolean()

    @classmethod
    def mutate(cls, root, info, **input):
        obj, created = cls.model.objects.get_or_create(**input)
        return cls(obj=obj, created=created)


class UpdateMutation(graphene.Mutation):
    @classmethod
    def mutate(cls, root, info, **input):
        obj = exists_or_raise(cls.model, input['id'])

        input.pop('id')
        for key, value in input.items():
            setattr(obj, key, value)
        obj.save(update_fields=input.keys())

        return cls(obj=obj)


class DeleteMutation(graphene.Mutation):
    ok = graphene.Boolean()

    @classmethod
    def mutate(cls, root, info, **input):
        obj = exists_or_raise(cls.model, input['id'])
        obj.delete()
        return cls(ok=True)
