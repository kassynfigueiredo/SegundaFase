# Generated by Django 3.2.6 on 2021-08-25 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicativo', '0002_alter_empresas_cnpj'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empresas',
            name='cnpj',
            field=models.IntegerField(),
        ),
    ]
