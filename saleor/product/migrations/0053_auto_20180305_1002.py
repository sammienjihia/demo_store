# Generated by Django 2.0.2 on 2018-03-05 16:02

from django.db import migrations
import versatileimagefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0052_slug_field_length'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='background_image',
            field=versatileimagefield.fields.VersatileImageField(blank=True, null=True, upload_to='category-backgrounds'),
        ),
        migrations.AddField(
            model_name='collection',
            name='background_image',
            field=versatileimagefield.fields.VersatileImageField(blank=True, null=True, upload_to='collection-backgrounds'),
        ),
    ]
