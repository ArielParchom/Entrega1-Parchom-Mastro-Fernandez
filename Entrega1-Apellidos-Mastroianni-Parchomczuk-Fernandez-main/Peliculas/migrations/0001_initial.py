# Generated by Django 4.1.1 on 2022-10-27 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pelicula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.TextField(max_length=30)),
                ('genero', models.TextField(max_length=20)),
                ('precio', models.FloatField()),
                ('duracion', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField(max_length=50)),
                ('mail', models.EmailField(max_length=254)),
                ('localidad', models.TextField(max_length=50)),
            ],
        ),
    ]
