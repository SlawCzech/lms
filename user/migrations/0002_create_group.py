import os

from django.db import migrations


def create_group(apps, schema_editor):
    Group = apps.get_model('auth', 'Group')

    Group.objects.create(name=os.environ.get('DJ_GROUP_STUDENTS'))
    Group.objects.create(name=os.environ.get('DJ_GROUP_INSTRUCTORS'))


def delete_group(apps, schema_editor):
    Group = apps.get_model('auth', 'Group')

    Group.objects.get(name=os.environ.get('DJ_GROUP_STUDENTS')).delete()
    Group.objects.get(name=os.environ.get('DJ_GROUP_INSTRUCTORS')).delete()


class Migration(migrations.Migration):
    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_group, delete_group)
    ]