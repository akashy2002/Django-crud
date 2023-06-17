# Generated by Django 4.1.7 on 2023-06-10 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0003_delete_crudcard_registration_address_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Crudcard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roll', models.CharField(blank=True, max_length=30, null=True)),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
                ('email', models.EmailField(blank=True, max_length=50, null=True)),
                ('phone', models.BigIntegerField(default=0)),
                ('address', models.TextField(blank=True, max_length=500, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='registration',
            name='address',
        ),
        migrations.RemoveField(
            model_name='registration',
            name='name',
        ),
        migrations.RemoveField(
            model_name='registration',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='registration',
            name='roll',
        ),
    ]
