# Generated by Django 5.0.4 on 2024-05-08 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_employees_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employees',
            name='address',
            field=models.TextField(),
        ),
    ]
