# Generated by Django 3.1.4 on 2021-01-03 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articleapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='created_at',
            field=models.DateField(auto_created=True, null=True),
        ),
    ]
