# Generated by Django 3.1.2 on 2020-10-13 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sightings', '0006_auto_20201013_0529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='squirrel',
            name='date',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='unique_squirrel_id',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
