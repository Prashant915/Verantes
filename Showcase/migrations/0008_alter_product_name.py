# Generated by Django 4.1.7 on 2024-01-08 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Showcase', '0007_alter_all_product_catogory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
