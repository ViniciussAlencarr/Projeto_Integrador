# Generated by Django 3.1.7 on 2021-03-27 02:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_pagamento'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resultado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score_Cliente', models.IntegerField()),
                ('id_Cliente', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='app.cliente')),
            ],
        ),
    ]
