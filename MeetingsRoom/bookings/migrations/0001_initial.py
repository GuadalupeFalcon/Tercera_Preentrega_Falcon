# Generated by Django 5.0.3 on 2024-04-16 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_de_usuario', models.CharField(max_length=50)),
                ('sala', models.CharField(max_length=50)),
            ],
        ),
    ]
