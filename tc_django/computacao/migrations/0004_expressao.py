# Generated by Django 3.2 on 2021-05-16 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('computacao', '0003_maquina'),
    ]

    operations = [
        migrations.CreateModel(
            name='Expressao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.CharField(max_length=100)),
                ('regex', models.CharField(max_length=100)),
            ],
        ),
    ]