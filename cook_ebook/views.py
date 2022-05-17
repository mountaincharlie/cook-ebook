from django.shortcuts import render
from django.views import generic, View
from .models import Recipe


# viewing the recipes on the homepage
class RecipeList(generic.ListView):
    # table model to use
    model = Recipe
    # filtering only public recipes
    queryset = Recipe.objects.filter(public_status=1).order_by("-created_date")
    template_name = "index.html"
