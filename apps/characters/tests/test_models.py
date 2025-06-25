import pytest

from apps.characters.models import Character


@pytest.mark.django_db
def test_create_character():
    character = Character.objects.create(
        name="Yoda",
        gender="male",
        birth_year="896BBY"
    )
    assert character.name == "Yoda"
