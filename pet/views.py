from django.shortcuts import render
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

class listPet(ListView):
    model = formPet
    queryset = formPet.objects.all()

class updatePet(UpdateView):
    model = formPet
    fields = '__all__'
    success_url = reverse_lazy('pet:list')

class detailPet(DetailView):
    queryset = formPet.objects.all()

class deletePet(DeleteView):
    queryset = formPet.objects.all()
    success_url = reverse_lazy('pet:list')

    

