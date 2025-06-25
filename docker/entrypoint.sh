#!/bin/bash
python manage.py makemigrations
python manage.py migrate

echo "🔍 Checking if characters exist..."
python manage.py shell -c "
from apps.characters.models import Character;
import sys;
sys.exit(0) if Character.objects.exists() else sys.exit(1)
"

if [ $? -ne 0 ]; then
    echo "🚀 No characters found, importing from SWAPI..."
    python manage.py import_swapi_data
else
    echo "✅ Characters already present — skipping SWAPI import."
fi

exec python manage.py runserver 0.0.0.0:8000