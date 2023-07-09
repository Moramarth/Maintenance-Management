# Generated by Django 4.2.1 on 2023-07-09 06:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdditionalAddressInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section', models.CharField(blank=True, max_length=50, null=True)),
                ('floor', models.IntegerField()),
                ('office_number', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=200)),
                ('tenants', models.ManyToManyField(through='estate.AdditionalAddressInformation', to='common.company')),
            ],
        ),
        migrations.AddField(
            model_name='additionaladdressinformation',
            name='building',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estate.building'),
        ),
        migrations.AddField(
            model_name='additionaladdressinformation',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.company'),
        ),
    ]
