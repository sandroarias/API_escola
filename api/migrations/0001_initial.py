# Generated by Django 3.2.15 on 2022-08-31 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Escola',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('cpf', models.CharField(max_length=13)),
                ('datanc', models.DateField()),
            ],
            options={
                'verbose_name': 'Escola',
                'verbose_name_plural': 'Escolas',
            },
        ),
    ]
