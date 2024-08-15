# Generated by Django 5.0.3 on 2024-08-11 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventos',
            name='gratuito',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='eventos',
            name='data_inicio',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='eventos',
            name='descricao',
            field=models.CharField(max_length=400),
        ),
    ]
