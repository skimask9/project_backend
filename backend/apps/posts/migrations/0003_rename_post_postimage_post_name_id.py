# Generated by Django 4.1.1 on 2022-09-22 16:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0002_alter_post_body_postimage"),
    ]

    operations = [
        migrations.RenameField(
            model_name="postimage",
            old_name="post",
            new_name="post_name_id",
        ),
    ]