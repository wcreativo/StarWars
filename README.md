# ⭐ Star Wars GraphQL API

A Django + GraphQL API (Relay-compatible) for exploring Star Wars characters, movies, and planets.

Built for scalability, testing, and developer happiness.

---

## 🚀 Features

- GraphQL API with [Relay](https://relay.dev/) support
- Real data from [SWAPI](https://swapi.dev/)
- Dockerized for easy deployment
- Includes mutations to create characters, planets, and movies
- Supports pagination, filtering, and nested querying

---

## 🛠️ Tech Stack

- Python 3.11+
- Django 4+
- [Graphene](https://graphene-python.org/)
- Relay-compatible schema
- PostgreSQL
- Docker / Docker Compose

---

## ⚙️ Installation (Dev)

### 1. Clone the repo

```bash
   git clone https://github.com/wcreativo/StarWars
   cd StarWars
```

### 2. Build and run with Docker

```bash
  docker-compose up --build
```

> First run will auto-import Star Wars data from SWAPI.

---

## 🧪 GraphQL Usage

GraphQL is available at:

```
http://localhost:8000/graphql/
```

---

## 📘 Example Queries

### 🧑‍🚀 All Characters (Relay Pagination)

#### Request

```graphql
query {
  allCharacters(first: 3) {
    edges {
      node {
        id
        name
        gender
        movies {
          title
        }
      }
      cursor
    }
    pageInfo {
      hasNextPage
      hasPreviousPage
      startCursor
      endCursor
    }
  }
}
```

#### Response

```json
{
  "data": {
    "allCharacters": {
      "edges": [
        {
          "node": {
            "id": "Q2hhcmFjdGVyVHlwZTox",
            "name": "Luke Skywalker",
            "gender": "male",
            "movies": [
              {
                "title": "A New Hope"
              }
            ]
          },
          "cursor": "YXJyYXljb25uZWN0aW9uOjA="
        }
        ...
      ],
      "pageInfo": {
        "hasNextPage": true,
        "startCursor": "...",
        "endCursor": "..."
      }
    }
  }
}
```

---

## ✍️ Example Mutation

### Create a Character

```graphql
mutation {
  createCharacter(
    name: "Leia Organa",
    gender: "female",
    birthYear: "19BBY",
    movieIds: [1]
  ) {
    character {
      name
      movies {
        title
      }
    }
  }
}
```

---

## 🔎 Filter Characters by Name

### Request

```graphql
query {
  allCharacters(name_Icontains: "Leia", first: 5) {
    edges {
      node {
        id
        name
        gender
        movies {
          title
        }
      }
    }
    pageInfo {
      hasNextPage
    }
  }
}
```

---

## 🐳 Docker Commands

### Rebuild containers

```bash
  docker-compose down -v
  docker-compose up --build
```

### Access Django shell

```bash
  docker-compose exec web python manage.py shell
```

### Import data manually

```bash
  docker-compose exec web python manage.py import_swapi_data
```

---

## 🧼 Reset Database (Dev Only)

To fully reset and re-import data:

```bash
  docker-compose down -v
  docker-compose up --build
```