# Generated by Django 3.2.4 on 2021-07-03 21:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0004_rename_location_name_location_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={},
        ),
        migrations.RenameField(
            model_name='location',
            old_name='name',
            new_name='location_name',
        ),
    ]