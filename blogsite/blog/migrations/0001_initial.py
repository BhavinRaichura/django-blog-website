# Generated by Django 4.0.1 on 2022-01-31 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=200)),
                ('phone_number', models.CharField(max_length=12)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
    ]
