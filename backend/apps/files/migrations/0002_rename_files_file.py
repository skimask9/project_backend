# Generated by Django 4.1.1 on 2022-09-29 18:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("files", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Files",
            new_name="File",
        ),
    ]
