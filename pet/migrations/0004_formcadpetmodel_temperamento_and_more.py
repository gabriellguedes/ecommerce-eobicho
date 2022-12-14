# Generated by Django 4.1 on 2022-08-31 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pet', '0003_formcadpetmodel_remove_caracteristicas_idnumber_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='formcadpetmodel',
            name='temperamento',
            field=models.CharField(choices=[('1', 'Agressivo'), ('2', 'Manso'), ('3', 'Anti-social'), ('4', 'Social'), ('5', 'Agitado'), ('6', 'Calmo'), ('7', 'Introvertido'), ('8', 'Extrovertido'), ('9', 'Obediente'), ('10', 'Independente'), ('11', 'Curioso'), ('12', 'Indiferente'), ('13', 'Ousado'), ('14', 'Tímido')], default=0, max_length=3),
        ),
        migrations.AlterField(
            model_name='formcadpetmodel',
            name='especie',
            field=models.CharField(choices=[('1', 'Cachorro'), ('2', 'Gato'), ('3', 'Coelho'), ('4', 'Cavalo'), ('5', 'Peixe')], default=0, max_length=3),
        ),
        migrations.AlterField(
            model_name='formcadpetmodel',
            name='peso',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='formcadpetmodel',
            name='tamanho',
            field=models.IntegerField(),
        ),
    ]
