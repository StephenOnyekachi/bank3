# Generated by Django 4.2.1 on 2023-08-02 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0004_users_type_alter_users_account'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='fund',
            field=models.IntegerField(default=1111, null=True),
        ),
    ]
