# Generated by Django 4.1.7 on 2023-12-23 06:21

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('Showcase', '0004_alter_testimonials_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonials',
            name='Review',
            field=tinymce.models.HTMLField(max_length=300),
        ),
    ]