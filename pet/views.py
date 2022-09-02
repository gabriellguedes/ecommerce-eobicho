from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from datetime import datetime
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, UpdateView
from django.views.generic.edit import DeleteView
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
        return render(request, 'pet/formpet_form.html', context=context)
    else:
        form = CadastroPet(request.POST)
        if form.is_valid():
            pet = form.save()
            form = CadastroPet()
        
        context = {
            'form':form
        }
        
        return render(request, 'pet/formpet_form.html', context=context)

def paginacao(request):
    parametro_page = request.GET.get('page', '1')
    parametro_limit = request.GET.get('limit', '5')

    if not (parametro_limit.isdigit() and int(parametro_limit)>0):
        parametro_limit = '10'



    pets = formPet.objects.all()
    pets_paginator = Paginator(pets, parametro_limit)

    try:
        page = pets_paginator.page(parametro_page)
    except (EmptyPage, PageNotAnInteger):
        page = pets_paginator.page(1)

    context = {
        'items_list': ['5','10', '20', '30', '50'],
        'pets': page
    }
    return render(request, 'pet/formpet_list.html', context)



class updatePet(UpdateView):
    model = formPet
    fields = '__all__'
    success_url = reverse_lazy('pet:list')

class detailPet(DetailView):
    queryset = formPet.objects.all()

    
class deletePet(DeleteView):
    queryset = formPet.objects.all()
    success_url = reverse_lazy('pet:list')
    
