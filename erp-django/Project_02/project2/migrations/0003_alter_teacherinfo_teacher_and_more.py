# Generated by Django 5.0.2 on 2024-03-01 03:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project2', '0002_teacherinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacherinfo',
            name='Teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Teacher_info', to='project2.teacher'),
        ),
        migrations.AlterField(
            model_name='teacherinfo',
            name='TeacherEXP',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Teacher_info', to='project2.experience'),
        ),
    ]