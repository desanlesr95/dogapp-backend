# Generated by Django 4.2.5 on 2024-06-03 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_user_groups_user_is_superuser_user_user_permissions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='pet_type',
            field=models.IntegerField(default=None, null=True),
        ),
    ]
