# Generated by Django 3.2 on 2021-05-17 02:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_emprestimo_situacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emprestimo',
            name='id_Cliente',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.cliente'),
        ),
    ]
