# Generated by Django 4.2.16 on 2024-09-16 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_rename_remente_cartao_remetente'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartao',
            name='imagem',
            field=models.ImageField(default='', upload_to='produtos/'),
        ),
    ]
