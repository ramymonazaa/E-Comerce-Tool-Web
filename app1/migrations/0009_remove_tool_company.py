# Generated by Django 2.2.5 on 2022-04-27 15:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0008_auto_20220427_1534'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tool',
            name='company',
        ),
    ]
