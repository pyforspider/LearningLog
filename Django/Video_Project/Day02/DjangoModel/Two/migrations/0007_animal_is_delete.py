# Generated by Django 2.2.3 on 2019-08-01 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Two', '0006_animal'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='is_delete',
            field=models.BooleanField(default=False),
        ),
    ]
