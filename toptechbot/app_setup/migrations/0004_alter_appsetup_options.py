# Generated by Django 5.0 on 2023-12-10 21:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_setup', '0003_menulink_app_setup'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='appsetup',
            options={'verbose_name': 'Setup', 'verbose_name_plural': "Setup's"},
        ),
    ]
