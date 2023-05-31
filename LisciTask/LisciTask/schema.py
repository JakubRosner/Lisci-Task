import graphene
import core.graphql.schema

class Query(
    core.graphql.schema.Query
):
    node = graphene.Node.Field()


class Mutation(
    core.graphql.schema.Mutation
):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation, auto_camelcase=False)
