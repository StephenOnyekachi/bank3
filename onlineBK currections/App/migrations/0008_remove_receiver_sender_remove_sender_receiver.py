# Generated by Django 4.2.1 on 2023-08-08 21:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0007_alter_receiver_sender_alter_sender_receiver'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='receiver',
            name='sender',
        ),
        migrations.RemoveField(
            model_name='sender',
            name='receiver',
        ),
    ]