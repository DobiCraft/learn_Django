# Generated by Django 2.0.1 on 2018-01-16 08:57

from django.db import migrations
import tagging.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='tag',
            field=tagging.fields.TagField(blank=True, max_length=255),
        ),
    ]
