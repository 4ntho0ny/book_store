# Generated by Django 5.1.2 on 2024-10-13 22:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book_outlet', '0008_country_alter_address_options_book_published'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='published',
            new_name='published_countries',
        ),
    ]
