# Generated by Django 3.2.13 on 2022-05-02 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_rename_tag_post_post_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_tag',
            field=models.CharField(default='Uncategorized', max_length=70),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
