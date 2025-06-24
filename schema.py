import graphene
import apps.characters.schema
import apps.movies.schema
import apps.planets.schema

class Query(
    apps.characters.schema.Query,
    apps.movies.schema.Query,
    apps.planets.schema.Query,
    graphene.ObjectType
):
    pass

class Mutation(
    apps.characters.schema.Mutation,
    apps.movies.schema.Mutation,
    apps.planets.schema.Mutation,
    graphene.ObjectType
):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)