from django import forms
from .models import FormCadPetModel

class CadastroPet(forms.ModelForm):
	class Meta:
		model = FormCadPetModel
		fields = '__all__'
