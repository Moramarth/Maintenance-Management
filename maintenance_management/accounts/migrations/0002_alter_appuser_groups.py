# Generated by Django 4.2.1 on 2023-07-16 05:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appuser',
            name='groups',
            field=models.ForeignKey(help_text='The group this user belongs to. A user will get all permissions granted to their group.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups'),
        ),
    ]
