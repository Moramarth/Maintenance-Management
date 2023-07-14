# Generated by Django 4.2.1 on 2023-07-14 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supervisor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignments',
            name='assignment_status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Accepted', 'Accepted'), ('Rejected', 'Rejected')], default='Pending', max_length=8),
        ),
    ]
