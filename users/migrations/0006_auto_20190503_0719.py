# Generated by Django 2.2 on 2019-05-03 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_profile_futsal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='is_futsal_admin',
            field=models.BooleanField(default=True),
        ),
    ]
