# Generated by Django 4.2.1 on 2023-07-06 07:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EngineeringProfile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('phone_number', models.IntegerField()),
                ('profile_picture', models.ImageField(upload_to='')),
                ('expertise', models.CharField(choices=[('Networking', 'Networking'), ('Electrical', 'Electrical'), ('Plumbing', 'Plumbing'), ('Structural Integrity', 'Structural Integrity'), ('Security Systems', 'Security Systems'), ('Landscaping', 'Landscaping')], max_length=50)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.company')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
