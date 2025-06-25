import graphene
from graphene_django.types import DjangoObjectType

from apps.movies.models import Movie
from .models import Character


class CharacterType(DjangoObjectType):
    class Meta:
        model = Character
        fields = "__all__"


class Query(graphene.ObjectType):
    all_characters = graphene.List(CharacterType, name=graphene.String())

    def resolve_all_characters(self, info, name=None):
        if name:
            return Character.objects.filter(name__icontains=name)
        return Character.objects.all()


class CreateCharacter(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        birth_year = graphene.String()
        gender = graphene.String()
        movie_ids = graphene.List(graphene.ID)

    character = graphene.Field(CharacterType)

    def mutate(self, info, name, birth_year=None, gender=None, movie_ids=None):
        character = Character.objects.create(
            name=name,
            birth_year=birth_year,
            gender=gender,
        )
        if movie_ids:
            movies = Movie.objects.filter(id__in=movie_ids)
            character.movies.set(movies)

        return CreateCharacter(character=character)


class Mutation(graphene.ObjectType):
    create_character = CreateCharacter.Field()
