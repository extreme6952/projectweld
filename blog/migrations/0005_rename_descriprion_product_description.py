# Generated by Django 4.2.7 on 2023-11-27 20:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_rename_body_product_descriprion_product_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='descriprion',
            new_name='description',
        ),
    ]
