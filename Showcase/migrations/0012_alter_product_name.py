# Generated by Django 4.1.7 on 2024-01-08 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Showcase', '0011_alter_product_image_alter_product_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(choices=[('Moduler Kitchen Designs', 'Moduler Kitchen Designs'), ('Wordrobe Designs', 'Wordrobe Designs'), ('Vanity Unit Design', 'Vanity Unit Design'), ('Bar kitchen Designs', 'Bar kitchen Designs')], max_length=255),
        ),
    ]