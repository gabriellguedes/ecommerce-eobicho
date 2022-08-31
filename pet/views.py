from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .models import formPet
from .forms import CadastroPet

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

class listPet(ListView):
    model = formPet
    queryset = formPet.objects.all()
    

