# Generated by Django 4.2.5 on 2025-07-03 00:31

from django.db import migrations, models
import django.db.models.deletion
import mln.models.static.static


class Migration(migrations.Migration):

    dependencies = [
        ('mln', '0031_correct_message_templates'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messagebody',
            name='easy_replies',
            field=models.ManyToManyField(blank=True, related_name='+', to='mln.messagebody'),
        ),
        migrations.AlterField(
            model_name='moduleexecutioncost',
            name='module_item',
            field=models.ForeignKey(limit_choices_to=models.Q(('type', mln.models.static.static.ItemType['MODULE'])), on_delete=django.db.models.deletion.CASCADE, related_name='%(class)ss', to='mln.iteminfo'),
        ),
        migrations.AlterField(
            model_name='moduleguestyield',
            name='module_item',
            field=models.ForeignKey(limit_choices_to=models.Q(('type', mln.models.static.static.ItemType['MODULE'])), on_delete=django.db.models.deletion.CASCADE, related_name='%(class)ss', to='mln.iteminfo'),
        ),
        migrations.AlterField(
            model_name='modulemessage',
            name='module_item',
            field=models.ForeignKey(limit_choices_to=models.Q(('type', mln.models.static.static.ItemType['MODULE'])), on_delete=django.db.models.deletion.CASCADE, related_name='%(class)ss', to='mln.iteminfo'),
        ),
        migrations.AlterField(
            model_name='moduleowneryield',
            name='module_item',
            field=models.ForeignKey(limit_choices_to=models.Q(('type', mln.models.static.static.ItemType['MODULE'])), on_delete=django.db.models.deletion.CASCADE, related_name='%(class)ss', to='mln.iteminfo'),
        ),
    ]
