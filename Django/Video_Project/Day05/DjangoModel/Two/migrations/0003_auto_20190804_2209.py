# Generated by Django 2.2.3 on 2019-08-04 22:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Two', '0002_auto_20190804_2059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idcard',
            name='id_person',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='Two.Person'),
        ),
    ]