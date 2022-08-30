from django.db import models

class Cadastro(models.Model):
	nome = models.CharField(max_length=200)
	apelido = models.CharField(max_length=200)
	aniversario = models.DateTimeField()
	idade = models.IntegerField(default=0)


class Caracteristicas(models.Model):
	idnumber = models.ForeignKey(Cadastro, on_delete=models.CASCADE)
	peso = models.IntegerField(default=0)
	tamanho = models.IntegerField(default=0)

	


