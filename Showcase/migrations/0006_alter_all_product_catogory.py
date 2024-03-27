# Generated by Django 4.1.7 on 2023-12-23 13:19

from django.db import migrations
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('Showcase', '0005_alter_testimonials_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='all_product',
            name='catogory',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='product', chained_model_field='product', default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='Showcase.catagory'),
        ),
    ]