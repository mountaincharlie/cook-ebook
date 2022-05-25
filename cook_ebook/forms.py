from .models import Recipe, Ingredient, Method, Tag
from django import forms


class CreateRecipeForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Recipe Title'}))
    tags = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple,required=False, queryset=Tag.objects.all())
    upload_image = forms.ImageField(required=False)

    class Meta:
        model = Recipe
        exclude = (
            'chef',
            'public_status',
            'created_date',
            'chefs_kisses',
            'tags',
            'cover_image',
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
