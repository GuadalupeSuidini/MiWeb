# Generated by Django 4.0.6 on 2022-08-28 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('primApp', '0005_merge_20220827_2005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mascotas',
            name='vacunas',
            field=models.TextField(max_length=150),
        ),
    ]