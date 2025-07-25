# Generated by Django 4.2.5 on 2025-07-04 22:21

from django.db import migrations, models
import django.db.models.deletion
import mln.models.static.static


class Migration(migrations.Migration):

    dependencies = [
        ('mln', '0031_correct_message_templates'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='is_secret',
            field=models.BooleanField(default=False, help_text='If true, this user is a secret networker and should not be displayed in public friend lists.'),
        ),
    ]
