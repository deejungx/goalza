# Generated by Django 2.2 on 2019-04-30 09:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('phone_number', models.CharField(max_length=12, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='customuser',
            name='is_futsal_admin',
            field=models.BooleanField(default=False),
        ),
    ]
