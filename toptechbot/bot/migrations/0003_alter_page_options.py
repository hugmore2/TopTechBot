# Generated by Django 5.0 on 2023-12-11 20:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0002_category_page'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='page',
            options={'verbose_name': 'Page', 'verbose_name_plural': 'Pages'},
        ),
    ]
