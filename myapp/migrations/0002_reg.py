# Generated by Django 4.2.4 on 2023-08-09 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='reg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('number', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=100)),
                ('district', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('cnfrm_pswd', models.CharField(max_length=100)),
            ],
        ),
    ]
