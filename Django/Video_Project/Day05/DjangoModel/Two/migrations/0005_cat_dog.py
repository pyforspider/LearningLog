# Generated by Django 2.2.3 on 2019-08-05 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Two', '0004_customer_goods'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a_name', models.CharField(max_length=16)),
                ('c_food', models.CharField(max_length=32)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Dog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a_name', models.CharField(max_length=16)),
                ('d_legs', models.IntegerField(default=4)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
