# Generated by Django 4.2.3 on 2023-07-12 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('institute', '0008_alter_instituteprofile_created_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instituteprofile',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='listwidget',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='textwidget',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='widgetlistitem',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
