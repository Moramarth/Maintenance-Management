# Generated by Django 4.2.1 on 2023-07-15 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0005_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.PositiveIntegerField(choices=[(1, 'Very Bad'), (2, 'Bad'), (3, 'Good'), (4, 'Very good'), (5, 'Excellent')]),
        ),
    ]