# Generated by Django 4.0.4 on 2022-06-24 13:48

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_product_section_product_image_product_section_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='Product_Information',
        ),
        migrations.AddField(
            model_name='product',
            name='Product_information',
            field=ckeditor.fields.RichTextField(default=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='Description',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
