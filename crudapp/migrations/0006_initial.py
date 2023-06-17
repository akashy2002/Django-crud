# Generated by Django 4.1.7 on 2023-06-10 09:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('crudapp', '0005_delete_crudcard_delete_registration'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50, unique=True)),
                ('email', models.EmailField(max_length=40, unique=True)),
                ('password', models.CharField(max_length=50)),
                ('password2', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Crudcard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roll', models.CharField(blank=True, max_length=30, null=True)),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
                ('email', models.EmailField(blank=True, max_length=50, null=True)),
                ('phone', models.BigIntegerField(default=0)),
                ('address', models.TextField(blank=True, max_length=500, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crudapp.registration')),
            ],
        ),
    ]
