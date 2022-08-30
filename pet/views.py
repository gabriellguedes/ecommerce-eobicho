from django.shortcuts import render
from django.http import HttpResponse
from .models import Cadastro

def FormInfoPet(request):
	return render(request, 'formIDpets.html')

def FormInspecaoPet(request):
	return render(request, 'formInspecao.html')

def login(request):
	return render(request, 'login.html')

