# Generated by Django 3.1.5 on 2021-01-15 18:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20210115_1539'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='create_at',
            new_name='create',
        ),
    ]