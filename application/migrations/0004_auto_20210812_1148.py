# Generated by Django 3.2.5 on 2021-08-12 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0003_rename_points_submitted_closestpoints_points_string'),
    ]

    operations = [
        migrations.AddField(
            model_name='closestpoints',
            name='added',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='closestpoints',
            name='closest_pair',
            field=models.TextField(blank=True, null=True),
        ),
    ]