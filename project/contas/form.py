from django.forms import ModelForm
from contas.models import Transation, Category
from django import forms


class Transation_Form(ModelForm):
    class Meta:
        model = Transation
        fields = ['description', 'value', 'category', 'observation']
    



class Category_Form(ModelForm):
    class Meta:
        model = Category
        fields = ["user", 'name']


class Element_Form(forms.Form):
    name = forms.CharField(label='name',max_length=200)
    state = forms.BooleanField(required=False)

