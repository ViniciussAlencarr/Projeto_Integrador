# Generated by Django 3.2 on 2021-06-13 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_emprestimo_nomecliente'),
    ]

    operations = [
        migrations.AddField(
            model_name='formulario',
            name='nomeCliente',
            field=models.CharField(default=1.0, max_length=40),
            preserve_default=False,
        ),
    ]
