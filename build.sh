#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt

export PYTHONPATH=.
python manage.py collectstatic --no-input
python manage.py migrate

# Create initial BridgeIT Admin account
python manage.py shell -c "
from django.contrib.auth import get_user_model;
User = get_user_model();
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@bridgeit.local', 'BridgeIT2026!');
    print('BridgeIT Admin Created Successfully');
"
