# Generated by Django 5.0.6 on 2024-06-27 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_car_delete_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='id',
        ),
        migrations.AlterField(
            model_name='car',
            name='car_name',
            field=models.CharField(max_length=500, primary_key=True, serialize=False),
        ),
    ]
