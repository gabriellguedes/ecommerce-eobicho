from django.urls import path
from .views import FormCadPetModel, form, listPet
from . import views

app_name = 'pet'

urlpatterns = [
    path('', views.form, name="formulario" ),
    path('formInspecaoPet/', views.FormInspecaoPet, name='InspecaoPet' ),
    path('list', views.listPet.as_view(), name='form_list' ),
        
] 