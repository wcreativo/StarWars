import graphene
from graphene_django.types import DjangoObjectType

from .models import Movie


class MovieType(DjangoObjectType):
    class Meta:
        model = Movie
        fields = "__all__"


class Query(graphene.ObjectType):
    all_movies = graphene.List(MovieType)

    def resolve_all_movies(self, info):
        return Movie.objects.all()


class CreateMovie(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        opening_crawl = graphene.String()
        director = graphene.String()
        producers = graphene.String()
        release_date = graphene.types.datetime.Date()

    movie = graphene.Field(MovieType)

    def mutate(self, info, title, opening_crawl=None, director=None, producers=None, release_date=None):
        movie = Movie.objects.create(
            title=title,
            opening_crawl=opening_crawl,
            director=director,
            producers=producers,
            release_date=release_date,
        )
        return CreateMovie(movie=movie)


class Mutation(graphene.ObjectType):
    create_movie = CreateMovie.Field()
