# Generated by Django 4.2.3 on 2024-02-03 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('institute', '0010_rename_index_title_instituteprofile_super_admin_index_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='instituteprofile',
            name='date_of_estashment',
        ),
        migrations.AddField(
            model_name='instituteprofile',
            name='date_of_establishment',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
