# Generated by Django 2.2.3 on 2019-08-05 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_auto_20190805_1426'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='u_icon',
            field=models.FileField(upload_to='%Y/%m/%d/static'),
        ),
    ]