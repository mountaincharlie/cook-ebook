from .models import Recipe
from django import forms

class CreateRecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = (
            'title',
            'summary',
            'cover_image',
            'tags',
            'chef',
        )
