# Generated by Django 4.2.5 on 2023-10-11 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_user_last_login'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='mail',
            field=models.CharField(max_length=150, unique=True),
        ),
    ]
