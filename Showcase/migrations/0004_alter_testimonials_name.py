# Generated by Django 4.1.7 on 2023-12-23 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Showcase', '0003_testimonials_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonials',
            name='Name',
            field=models.CharField(max_length=40),
        ),
    ]