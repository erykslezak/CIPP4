# Generated by Django 3.2.13 on 2022-05-02 19:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20220502_1949'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='tag',
            new_name='post_tag',
        ),
    ]
