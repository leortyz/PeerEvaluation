# Generated by Django 2.2.5 on 2020-08-30 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evaluation', '0005_auto_20200721_1117'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='paralelo',
            field=models.IntegerField(default=2),
        ),
    ]
