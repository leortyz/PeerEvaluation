# Generated by Django 2.2.4 on 2020-07-21 02:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('evaluation', '0002_encuesta_evaluacion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='encuesta',
            name='fecha',
        ),
    ]
