# Generated by Django 3.2.4 on 2021-07-05 06:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0009_alter_image_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ['image']},
        ),
    ]