# Generated by Django 3.1.5 on 2022-01-16 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='main',
            name='name',
            field=models.TextField(default='None'),
        ),
    ]
