# Generated by Django 3.2.5 on 2021-11-09 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0002_auto_20211108_0217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cupom',
            name='valorDataHora',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='resultadomineracao',
            name='valorDataHora',
            field=models.DateField(),
        ),
    ]
