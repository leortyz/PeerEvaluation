# Generated by Django 2.2.4 on 2020-07-21 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evaluation', '0003_remove_encuesta_fecha'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='done',
            field=models.BooleanField(default=False),
        ),
    ]
