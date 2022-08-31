from django import forms
from .models import formPet

class CadastroPet(forms.ModelForm):
	class Meta:
		model = formPet
		fields = '__all__'
