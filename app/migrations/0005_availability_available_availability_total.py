# Generated by Django 4.0.6 on 2022-07-30 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_availability'),
    ]

    operations = [
        migrations.AddField(
            model_name='availability',
            name='available',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='availability',
            name='total',
            field=models.IntegerField(default=0),
        ),
    ]
