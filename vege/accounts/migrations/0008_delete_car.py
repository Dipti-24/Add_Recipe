# Generated by Django 4.2.4 on 2023-09-15 06:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_delete_customuser'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Car',
        ),
    ]