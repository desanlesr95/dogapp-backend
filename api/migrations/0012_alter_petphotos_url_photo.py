# Generated by Django 4.2.5 on 2024-07-05 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_petshare_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='petphotos',
            name='url_photo',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]
