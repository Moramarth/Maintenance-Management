# Generated by Django 4.2.1 on 2023-07-10 13:19

import django.core.validators
from django.db import migrations, models
import maintenance_management.accounts.validators


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appuserprofile',
            name='first_name',
            field=models.CharField(blank=True, max_length=30, null=True, validators=[django.core.validators.MinLengthValidator(2), maintenance_management.accounts.validators.only_letters_validator, maintenance_management.accounts.validators.first_char_validation]),
        ),
        migrations.AlterField(
            model_name='appuserprofile',
            name='last_name',
            field=models.CharField(blank=True, max_length=30, null=True, validators=[django.core.validators.MinLengthValidator(2), maintenance_management.accounts.validators.only_letters_validator, maintenance_management.accounts.validators.first_char_validation]),
        ),
        migrations.AlterField(
            model_name='appuserprofile',
            name='phone_number',
            field=models.CharField(blank=True, max_length=15, null=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')]),
        ),
        migrations.AlterField(
            model_name='appuserprofile',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='images', validators=[maintenance_management.accounts.validators.validate_file_size]),
        ),
        migrations.AlterField(
            model_name='registerinvitation',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='registerinvitation',
            name='secondary_email',
            field=models.EmailField(help_text='You will get a copy of the invitation to be sure sending was properly handled', max_length=254, verbose_name='Your Email:'),
        ),
    ]
