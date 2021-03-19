# Generated by Django 2.2.5 on 2019-11-03 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodapp', '0010_remove_item_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='cuisine',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='description',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
    ]