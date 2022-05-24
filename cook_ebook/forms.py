from .models import Recipe, Ingredient, Method
from django import forms


class CreateRecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        exclude = (
            'public_status',
            'created_date',
            'chefs_kisses',
        )


# credit: https://engineertodeveloper.com/getting-started-with-formsets-create-a-recipe-app/
class AddIngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        exclude = ('recipe',)


class AddMethodForm(forms.ModelForm):
    class Meta:
        model = Method
        exclude = ('recipe',)


AddIngredientFormSet = forms.inlineformset_factory(Recipe, Ingredient, form=AddIngredientForm)

AddMethodFormSet = forms.inlineformset_factory(Recipe, Method, form=AddMethodForm)
