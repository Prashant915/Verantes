# Generated by Django 4.1.7 on 2024-01-08 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Showcase', '0010_alter_product_image_alter_product_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Image',
            field=models.ImageField(default=None, upload_to='Catagories'),
        ),
        migrations.AlterField(
            model_name='product',
            name='Link',
            field=models.URLField(default=None),
        ),
    ]