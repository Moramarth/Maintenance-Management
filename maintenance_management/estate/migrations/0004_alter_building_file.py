# Generated by Django 4.2.1 on 2023-08-02 09:07

from django.db import migrations, models
import maintenance_management.accounts.validators


class Migration(migrations.Migration):

    dependencies = [
        ('estate', '0003_rename_picture_building_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='building',
            name='file',
            field=models.ImageField(blank=True, null=True, upload_to='images', validators=[maintenance_management.accounts.validators.validate_file_size], verbose_name='Picture'),
        ),
    ]