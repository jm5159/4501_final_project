# Generated by Django 3.1.2 on 2020-10-13 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sightings', '0010_auto_20201013_1737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='squirrel',
            name='unique_squirrel_id',
            field=models.CharField(max_length=100),
        ),
    ]