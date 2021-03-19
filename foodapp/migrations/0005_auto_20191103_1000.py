# Generated by Django 2.2.5 on 2019-11-03 04:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('foodapp', '0004_auto_20191102_1505'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='shot_size',
            field=models.IntegerField(choices=[(1, 'VEG'), (2, 'NON-VEG')], default=1),
        ),
        migrations.AddField(
            model_name='menucatalog',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='foodapp.Category'),
        ),
    ]