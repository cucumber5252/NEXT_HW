# Generated by Django 4.1.7 on 2023-04-06 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoApp', '0007_alter_post_deadline'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='done',
            field=models.BooleanField(default=False),
        ),
    ]
