# Generated by Django 5.0 on 2023-12-11 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appturnos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reserva',
            name='creado',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
