# Generated by Django 2.2.5 on 2019-11-03 06:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foodapp', '0007_remove_item_food_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menucatalog',
            name='category',
        ),
    ]
