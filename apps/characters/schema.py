import django_filters
import graphene
from graphene import relay
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.types import DjangoObjectType

from apps.movies.models import Movie
from .models import Character


class CharacterFilter(django_filters.FilterSet):
    class Meta:
        model = Character
        fields = {
            'name': ['icontains'],
            'birth_year': ['exact'],
            'gender': ['exact'],
        }


class CharacterType(DjangoObjectType):
    class Meta:
        model = Character
        interfaces = (relay.Node,)
        fields = "__all__"


class Query(graphene.ObjectType):
    node = relay.Node.Field()

    all_characters = DjangoFilterConnectionField(
        CharacterType,
        filterset_class=CharacterFilter,
    )


class CreateCharacter(relay.ClientIDMutation):
    class Input:
        name = graphene.String(required=True)
        birth_year = graphene.String()
        gender = graphene.String()
        movie_ids = graphene.List(graphene.ID)

    character = graphene.Field(CharacterType)

    @classmethod
    def mutate_and_get_payload(cls, root, info, **input):
        name = input.get('name')
        birth_year = input.get('birth_year')
        gender = input.get('gender')
        movie_ids = input.get('movie_ids')

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
