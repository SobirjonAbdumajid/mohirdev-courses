# Generated by Django 5.0.3 on 2024-03-28 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Costumer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fio', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('status', models.CharField(max_length=255)),
                ('dob', models.DateField()),
                ('dt', models.TimeField(auto_now_add=True)),
            ],
        ),
    ]
