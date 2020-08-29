# Generated by Django 2.2.4 on 2020-07-21 01:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('evaluation', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Encuesta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Evaluacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calificacion', models.PositiveIntegerField()),
                ('encuesta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='evaluation.Encuesta')),
                ('estudiante', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='evaluation.Student')),
            ],
        ),
    ]
