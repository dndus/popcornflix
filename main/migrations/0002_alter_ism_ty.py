# Generated by Django 3.2.2 on 2021-06-08 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ism',
            name='ty',
            field=models.CharField(max_length=15),
        ),
    ]