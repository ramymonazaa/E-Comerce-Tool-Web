# Generated by Django 2.2.5 on 2022-04-24 03:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_auto_20220424_0333'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='age',
        ),
    ]
