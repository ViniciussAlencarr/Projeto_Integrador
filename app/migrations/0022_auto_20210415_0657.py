# Generated by Django 3.1.7 on 2021-04-15 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0021_auto_20210415_0655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ficha_cadastral',
            name='senha_Cliente',
            field=models.CharField(max_length=15),
        ),
    ]