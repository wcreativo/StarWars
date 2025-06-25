import requests
from django.core.management.base import BaseCommand

from apps.characters.models import Character
from apps.movies.models import Movie
from apps.planets.models import Planet


class Command(BaseCommand):
    help = "Import Star Wars data from SWAPI"

    def handle(self, *args, **options):
        self.import_planets()
        movies = self.import_movies()
        self.import_characters(movies)
        print("✅ Done importing Star Wars data.")

    def import_planets(self):
        print("🌍 Importing planets...")
        url = "https://swapi.py4e.com/api/planets/"
        while url:
            res = requests.get(url).json()
            for p in res["results"]:
                Planet.objects.update_or_create(
                    name=p["name"],
                    defaults={
                        "climate": p.get("climate", ""),
                        "terrain": p.get("terrain", ""),
                    },
                )
            url = res["next"]

    def import_movies(self):
        print("🎬 Importing movies...")
        url = "https://swapi.py4e.com/api/films/"
        res = requests.get(url).json()
        movies = {}
        for m in res["results"]:
            movie_obj, _ = Movie.objects.update_or_create(
                title=m["title"],
                defaults={
                    "opening_crawl": m["opening_crawl"],
                    "director": m["director"],
                    "producers": m["producer"],
                    "release_date": m["release_date"],
                },
            )

            # Link planets
            movie_planets = []
            for planet_url in m["planets"]:
                planet_data = requests.get(planet_url).json()
                planet = Planet.objects.filter(name=planet_data["name"]).first()
                if planet:
                    movie_planets.append(planet)
            movie_obj.planets.set(movie_planets)
            movies[m["url"]] = movie_obj
        return movies

    def import_characters(self, movies_map):
        print("🧑‍🚀 Importing characters...")
        url = "https://swapi.py4e.com/api/people/"
        while url:
            res = requests.get(url).json()
            for c in res["results"]:
                character, _ = Character.objects.update_or_create(
                    name=c["name"],
                    defaults={
                        "birth_year": c.get("birth_year", ""),
                        "gender": c.get("gender", ""),
                    },
                )

                # Link to movies
                related_movies = [
                    movies_map[m_url] for m_url in c["films"] if m_url in movies_map
                ]
                character.movies.set(related_movies)
            url = res["next"]
