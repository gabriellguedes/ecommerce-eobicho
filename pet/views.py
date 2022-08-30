from django.shortcuts import render
from django.http import HttpResponse

def FormInfoPet(request):
	return render(request, 'formIDpets.html')

def FormInspecaoPet(request):
	return render(request, 'formInspecao.html')