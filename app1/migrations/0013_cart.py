# Generated by Django 2.2.5 on 2022-05-13 23:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0012_auto_20220505_0106'),
    ]

    operations = [
        migrations.CreateModel(
            name='cart',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='')),
                ('expiration_date', models.FloatField()),
                ('price', models.FloatField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, related_name='cart', to='app1.category')),
            ],
        ),
    ]