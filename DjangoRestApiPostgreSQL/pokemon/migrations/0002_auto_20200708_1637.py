# Generated by Django 3.0.8 on 2020-07-08 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tipo',
            name='name',
            field=models.CharField(default='', max_length=45, unique=True),
        ),
    ]
