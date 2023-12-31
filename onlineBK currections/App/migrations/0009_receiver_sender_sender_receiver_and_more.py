# Generated by Django 4.2.1 on 2023-08-08 21:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0008_remove_receiver_sender_remove_sender_receiver'),
    ]

    operations = [
        migrations.AddField(
            model_name='receiver',
            name='sender',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='sender',
            name='receiver',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='receiver',
            name='receiver',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='sender',
            name='sender',
            field=models.TextField(null=True),
        ),
    ]
