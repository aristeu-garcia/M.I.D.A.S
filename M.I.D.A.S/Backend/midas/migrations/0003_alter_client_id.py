# Generated by Django 5.0.2 on 2024-03-11 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('midas', '0002_client'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]