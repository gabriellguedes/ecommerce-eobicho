# Generated by Django 4.1 on 2022-08-31 17:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pet', '0007_alter_formcadpetmodel_caracteristicas_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='FormCadPetModel',
            new_name='formPet',
        ),
    ]
