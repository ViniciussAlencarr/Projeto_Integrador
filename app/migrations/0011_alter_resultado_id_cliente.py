# Generated by Django 3.2 on 2021-06-15 04:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20210614_2115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resultado',
            name='id_Cliente',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.cliente'),
        ),
    ]
