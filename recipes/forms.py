from django import forms
from .models import Recipe, RecipeIngredients

def RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name', 'description', 'directions']
