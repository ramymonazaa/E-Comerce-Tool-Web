# Generated by Django 2.2.5 on 2022-04-27 15:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0007_auto_20220427_1529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tool',
            name='category',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, related_name='category', to='app1.category'),
        ),
    ]
