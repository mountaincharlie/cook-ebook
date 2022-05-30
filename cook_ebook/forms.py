"""
Django's forms.py for creating the forms I use in views.py
credit:
https://engineertodeveloper.com/getting-started-with-formsets-create-a-recipe-app/
for how to create the inline formset for ingredient
which I also then used for method
"""

from django import forms
from .models import Recipe, Ingredient, Method, Tag


class CreateRecipeForm(forms.ModelForm):
    """
    Creating the create recipe form from Django's
    forms.ModelForm
    Sets placeholder text for the title field.
    Sets the tags field as CheckboxSelectMultiple
    using a Django widget.
    Sets the cover_imaeg field as ImageField since
    CloudinaryField does not work here.

    Excluding the recipe fields:
    -chef (automatically set as the user)
    -public_status (automatically set as private)
    -created_date (automatically set as time created)
    -chefs_kisses (not a required field)
    -tags (manually set as CheckboxSelectMultiple)
    -cover_image (manually set as ImageField)
    -slug (automatically set by models' random_slug method)
    """
    title = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Recipe Title'})
    )
    tags = forms.ModelMultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        required=False,
        queryset=Tag.objects.all()
    )
    upload_image = forms.ImageField(required=False)

    class Meta:
        """ meta data for CreateRecipeForm """
        model = Recipe
        exclude = (
            'chef',
            'public_status',
            'created_date',
            'chefs_kisses',
            'tags',
            'cover_image',
            'slug',
        )


class AddIngredientForm(forms.ModelForm):
    """
    Creating the add ingredient form from Django's
    forms.ModelForm
    Excluding the recipe field from the Ingredient
    table model
    """
    class Meta:
        """ meta data for AddIngredientForm """
        model = Ingredient
        exclude = ('recipe',)


class AddMethodForm(forms.ModelForm):
    """
    Creating the add method form from Django's
    forms.ModelForm
    Excluding the recipe field from the Method
    table model
    """
    class Meta:
        """ meta data for AddMethodForm """
        model = Method
        exclude = ('recipe',)


AddIngredientFormSet = forms.inlineformset_factory(
    Recipe,
    Ingredient,
    form=AddIngredientForm,
    extra=0
)

AddMethodFormSet = forms.inlineformset_factory(
    Recipe,
    Method,
    form=AddMethodForm,
    extra=0
)
