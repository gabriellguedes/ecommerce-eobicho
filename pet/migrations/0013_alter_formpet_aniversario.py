# Generated by Django 4.1 on 2022-09-01 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pet', '0012_alter_formpet_aniversario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formpet',
            name='aniversario',
            field=models.DateField(blank=True, null=True, verbose_name='Aniversário'),
        ),
    ]
