# Generated by Django 3.2 on 2021-05-12 16:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0026_alter_administrador_id_cliente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emprestimo',
            name='id_Cliente',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='app.cliente'),
        ),
    ]
