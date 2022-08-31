from django.shortcuts import render
from django.http import HttpResponse
from .models import FormCadPetModel
from .forms import CadastroPet

def FormInfoPet(request):
	return render(request, 'formIDpets.html')

def FormInspecaoPet(request):
	return render(request, 'formInspecao.html')

def form(request):
    if request.method == 'GET':
        form = CadastroPet()
        context = {
            'form':form
        }
        return render(request, 'form.html', context=context)
    else:
        form = CadastroPet(request.POST)
        if form.is_valid():
            pet = form.save()
            form = CadastroPet()
        
        context = {
            'form':form
        }
        return render(request, 'form.html', context=context)

