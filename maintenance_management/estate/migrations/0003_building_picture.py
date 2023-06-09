# Generated by Django 4.2.1 on 2023-07-13 00:01

from django.db import migrations, models
import maintenance_management.accounts.validators


class Migration(migrations.Migration):

    dependencies = [
        ('estate', '0002_alter_building_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='building',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='images', validators=[maintenance_management.accounts.validators.validate_file_size]),
        ),
    ]
