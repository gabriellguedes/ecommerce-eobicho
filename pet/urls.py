from django.urls import path
#from .views import form, listPet
from . import views

app_name = 'pet'

urlpatterns = [
    path('', views.form, name='form' ),
    path('list', views.paginacao, name='list'),
    path('update/<int:pk>/', views.updatePet.as_view(), name='update'),
    path('detail/<int:pk>/', views.detailPet.as_view(), name='detail'),
    path('delete/<int:pk>/', views.deletePet.as_view(), name='delete'),
    path('formInspecaoPet/', views.FormInspecaoPet, name='InspecaoPet'),
        
] 
