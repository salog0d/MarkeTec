# Generated by Django 5.1.7 on 2025-03-08 02:06

import authentication.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20, unique=True)),
                ('name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('bio', models.CharField(max_length=200)),
                ('age', models.IntegerField(validators=[django.core.validators.MinValueValidator(18), django.core.validators.MaxValueValidator(100)])),
                ('email', models.EmailField(max_length=254, unique=True, validators=[authentication.models.User.validate_email_domain])),
                ('campus', models.CharField(choices=[('AGS', 'Aguascalientes'), ('CHP', 'Chiapas'), ('CHI', 'Chihuahua'), ('CDMX', 'Mexico City'), ('CJZ', 'Ciudad Juárez'), ('CVA', 'Cuernavaca'), ('CEM', 'State of Mexico'), ('GDL', 'Guadalajara'), ('HGO', 'Hidalgo'), ('IRA', 'Irapuato'), ('LAG', 'Laguna'), ('LEO', 'León'), ('MTY', 'Monterrey'), ('MOR', 'Morelia'), ('PUE', 'Puebla'), ('QRO', 'Querétaro'), ('SLP', 'San Luis Potosí'), ('CSF', 'Santa Fe'), ('SIN', 'Sinaloa'), ('SON', 'Sonora Norte'), ('TAM', 'Tampico'), ('TOL', 'Toluca'), ('VER', 'Veracruz'), ('ZAC', 'Zacatecas')], max_length=10)),
            ],
        ),
    ]
