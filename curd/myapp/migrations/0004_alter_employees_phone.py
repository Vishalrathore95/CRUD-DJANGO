# Generated by Django 5.0.4 on 2024-05-08 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_alter_employees_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employees',
            name='phone',
            field=models.BigIntegerField(),
        ),
    ]
