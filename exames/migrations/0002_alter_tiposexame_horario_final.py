# Generated by Django 4.2.5 on 2023-10-04 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exames', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tiposexame',
            name='horario_final',
            field=models.IntegerField(),
        ),
    ]