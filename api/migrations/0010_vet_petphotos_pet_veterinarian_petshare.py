# Generated by Django 4.2.5 on 2024-06-03 23:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_petphotos'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('logo', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('ubication', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='petphotos',
            name='pet',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.pet'),
        ),
        migrations.CreateModel(
            name='Veterinarian',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('identification', models.CharField(max_length=50)),
                ('years_experience', models.IntegerField()),
                ('work_in', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.vet')),
            ],
        ),
        migrations.CreateModel(
            name='PetShare',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('pet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.pet')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
