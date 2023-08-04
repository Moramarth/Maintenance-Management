# Generated by Django 4.2.1 on 2023-08-02 09:07

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_appuser_groups'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appuserprofile',
            name='phone_number',
            field=models.CharField(blank=True, max_length=15, null=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+\\d{9,15}$')]),
        ),
    ]