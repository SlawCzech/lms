import os

from django.contrib.auth import get_user_model
from django.db import migrations


def create_super_user(apps, schema_editor):
    User = get_user_model()

    DJANGO_SU_NAME = os.environ.get('DJANGO_SU_NAME')
    DJANGO_SU_EMAIL = os.environ.get('DJANGO_SU_EMAIL')
    DJANGO_SU_PASSWORD = os.environ.get('DJANGO_SU_PASSWORD')

    User.objects.create_superuser(
        fullname=DJANGO_SU_NAME,
        email=DJANGO_SU_EMAIL,
        password=DJANGO_SU_PASSWORD
    )


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_create_group'),
    ]

    operations = [
        migrations.RunPython(create_super_user)
    ]
