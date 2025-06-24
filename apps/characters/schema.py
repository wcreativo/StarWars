import graphene
from graphene_django.types import DjangoObjectType

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
        height = graphene.Int()
        mass = graphene.Float()

    character = graphene.Field(CharacterType)

    def mutate(self, info, name, birth_year=None, gender=None, height=None, mass=None):
        character = Character.objects.create(
            name=name,
            birth_year=birth_year,
            gender=gender,
            height=height,
            mass=mass
        )
        return CreateCharacter(character=character)


class Mutation(graphene.ObjectType):
    create_character = CreateCharacter.Field()
