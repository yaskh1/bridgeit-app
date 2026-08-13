#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt

export PYTHONPATH=.
python manage.py collectstatic --no-input
python manage.py migrate

# Create or reset BridgeIT Admin account with full staff access
python manage.py shell -c "
from django.contrib.auth import get_user_model;
User = get_user_model();
if User.objects.filter(username='admin').exists():
    u = User.objects.get(username='admin')
    u.set_password('BridgeIT2026!')
    u.is_staff = True
    u.is_superuser = True
    u.save()
else:
    User.objects.create_superuser(username='admin', email='admin@bridgeit.local', password='BridgeIT2026!', is_staff=True, is_superuser=True)
print('BridgeIT Admin updated successfully.')
"
