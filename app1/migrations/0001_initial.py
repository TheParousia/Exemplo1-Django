# Generated by Django 5.1 on 2024-08-29 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cartao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('remente', models.CharField(max_length=30)),
                ('mensagem', models.TextField(max_length=255)),
            ],
        ),
    ]