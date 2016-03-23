from django import forms
from django.core.validators import RegexValidator
from main.model import City


alphanumeric = RegexValidator(r'^[a-sA-Z]*$','Only alphanumeric characters are allowed')

class CitySearchForm (forms.Form):
	name = forms.CharField(required=True , initial='Orem', validators=[alphanumeric])
	state = forms.CharField(required=True,initial='utah',validators=[alphanumeric])


class CreateCityForm(forms.ModelForm):
	class Meta:
		model = City
		fields = '__all__'

