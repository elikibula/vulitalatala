# Generated by Django 2.2.13 on 2021-03-26 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notices', '0003_auto_20210326_1300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='expires_at',
            field=models.DateField(),
        ),
    ]
