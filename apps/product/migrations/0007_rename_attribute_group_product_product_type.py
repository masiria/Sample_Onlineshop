# Generated by Django 4.2 on 2024-06-16 05:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_product_attribute_group'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='attribute_group',
            new_name='product_type',
        ),
    ]
