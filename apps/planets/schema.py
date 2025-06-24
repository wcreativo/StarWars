import graphene
from graphene_django.types import DjangoObjectType

from .models import Planet


class PlanetType(DjangoObjectType):
    class Meta:
        model = Planet
        fields = '__all__'


class Query(graphene.ObjectType):
    all_planets = graphene.List(PlanetType)

    def resolve_all_planets(self, info):
        return Planet.objects.all()


class CreatePlanet(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        climate = graphene.String()
        terrain = graphene.String()
        population = graphene.String()

    planet = graphene.Field(PlanetType)

    def mutate(self, info, name, climate=None, terrain=None, population=None):
        planet = Planet.objects.create(
            name=name,
            climate=climate,
            terrain=terrain,
            population=population
        )
        return CreatePlanet(planet=planet)


class Mutation(graphene.ObjectType):
    create_planet = CreatePlanet.Field()
