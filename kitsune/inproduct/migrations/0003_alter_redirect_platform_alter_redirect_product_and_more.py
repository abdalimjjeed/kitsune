# Generated by Django 4.1.7 on 2023-03-23 03:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("inproduct", "0002_increase_max_lengths"),
    ]

    operations = [
        migrations.AlterField(
            model_name="redirect",
            name="platform",
            field=models.CharField(blank=True, db_index=True, max_length=50),
        ),
        migrations.AlterField(
            model_name="redirect",
            name="product",
            field=models.CharField(blank=True, db_index=True, max_length=50),
        ),
        migrations.AlterField(
            model_name="redirect",
            name="topic",
            field=models.CharField(blank=True, db_index=True, max_length=100),
        ),
        migrations.AlterField(
            model_name="redirect",
            name="version",
            field=models.CharField(blank=True, db_index=True, max_length=50),
        ),
    ]
