# Generated by Django 4.0.6 on 2022-07-29 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_booking_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='Phone_number',
            field=models.CharField(max_length=200),
        ),
    ]
