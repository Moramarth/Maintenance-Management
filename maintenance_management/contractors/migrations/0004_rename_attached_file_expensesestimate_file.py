# Generated by Django 4.2.1 on 2023-08-02 09:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contractors', '0003_alter_meeting_meeting_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='expensesestimate',
            old_name='attached_file',
            new_name='file',
        ),
    ]
