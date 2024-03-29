# Generated by Django 4.2.1 on 2023-08-02 09:17

from django.db import migrations, models
import maintenance_management.accounts.validators


class Migration(migrations.Migration):

    dependencies = [
        ('contractors', '0004_rename_attached_file_expensesestimate_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expensesestimate',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='documents', validators=[maintenance_management.accounts.validators.validate_file_size], verbose_name='Attached File'),
        ),
    ]
