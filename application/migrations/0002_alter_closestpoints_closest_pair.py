# Generated by Django 3.2.5 on 2021-07-28 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='closestpoints',
            name='closest_pair',
            field=models.TextField(),
        ),
    ]