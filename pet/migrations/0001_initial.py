# Generated by Django 4.1 on 2022-08-30 17:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FormCadastro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('apelido', models.CharField(max_length=200)),
                ('aniversario', models.DateTimeField()),
                ('idade', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='FormCaracteristicas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('peso', models.IntegerField(default=0)),
                ('tamanho', models.IntegerField(default=0)),
                ('idnumber', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pet.formcadastro')),
            ],
        ),
    ]
