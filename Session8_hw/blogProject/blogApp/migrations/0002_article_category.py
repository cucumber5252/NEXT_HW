# Generated by Django 4.1.7 on 2023-04-04 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.TextField(default=''),
        ),
    ]
