# Generated by Django 4.2.1 on 2023-07-30 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='account',
            field=models.IntegerField(default=0, null=True),
        ),
    ]