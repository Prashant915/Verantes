# Generated by Django 4.1.7 on 2023-12-28 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Customer_Requirement', '0002_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AddField(
            model_name='profile',
            name='pincode',
            field=models.CharField(default=None, max_length=6),
        ),
    ]