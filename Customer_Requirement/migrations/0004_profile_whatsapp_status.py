# Generated by Django 4.1.7 on 2023-12-29 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Customer_Requirement', '0003_profile_email_profile_pincode'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='whatsapp_status',
            field=models.CharField(default=None, max_length=10),
        ),
    ]