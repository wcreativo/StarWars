import pytest
from graphene.test import Client

from schema import schema


@pytest.mark.django_db
def test_create_character_mutation():
    client = Client(schema)
    query = '''
        mutation {
          createCharacter(input: {
            name: "Obi-Wan Kenobi",
            gender: "male",
            birthYear: "57BBY",
            movieIds: ["1"]
          }) {
            character {
              id
              name
              gender
              movies {
                title
              }
            }
          }
        }
    '''
    response = client.execute(query)
    assert response["data"]["createCharacter"]["character"]["name"] == "Obi-Wan Kenobi"
