# Generated by Django 3.1 on 2020-09-21 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20200921_1120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='rank',
            field=models.CharField(choices=[('Employee', 'Employee'), ('Manager', 'Manager')], default='Employee', max_length=100),
        ),
    ]
