from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from .models import Tag, Recipe
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User


# viewing the recipes on the homepage
class TagList(generic.ListView):
    # table model to use
    model = Tag
    queryset = Tag.objects.all()
    # the template to show the list in (as 'tag_list')
    template_name = "index.html"


class RecipeSearchView(generic.ListView):

    def get(self, request, *args, **kwargs):

        search_input = request.GET.get('search').replace(" ", "")
        recipes = Recipe.objects.filter(title__icontains=search_input).filter(public_status=1)

        # checking if search isnt blank and if any recipes title contain it
        if search_input != '' and recipes:
            context = {
                'recipes': recipes,
                'num_results': len(recipes)
            }
        else:
            context = {
                'recipes': 'none',
                'num_results': 0,
                'message': "No Public Recipe's titles contain all or part of this search"
            }
        return render(request, 'index.html', context)


class RecipeByTagView(generic.ListView):

    def get(self, request, *args, **kwargs):
        # getting all recipes with this tag (by its pk)
        recipes = Recipe.objects.filter(tags=self.kwargs['pk']).filter(public_status=1)
        print('This is recipes:', recipes)
        if len(recipes) != 0:
            context = {
                'recipes': recipes,
                'num_results': len(recipes)
            }
        else:
            context = {
                'recipes': 'none',
                'num_results': len(recipes),
                'message': 'No public Recipes have been assigned this tag yet'
            }
        return render(request, 'index.html', context)


class RecipeDetailsView(View):

    def get(self, request, *args, **kwargs):
        # getting all the recipes
        recipes = Recipe.objects.all()
        recipe = get_object_or_404(recipes, pk=self.kwargs['pk'])

        chefs_kiss = False
        if recipe.chefs_kisses.filter(id=self.request.user.id).exists():
            chefs_kiss = True

        context = {
            'recipe': recipe,
            'chefs_kiss': chefs_kiss,
        }

        return render(request, 'recipe_details.html', context)


class RecipeChefsKissView(View):
    # when the user clicks on the chefs kiss button
    def post(self, request, *args, **kwargs):
        # getting the recipe
        recipe = get_object_or_404(Recipe, pk=self.kwargs['pk'])

        # toggeling the btn highligh if the user has already clicked the btn
        if recipe.chefs_kisses.filter(id=request.user.id).exists():
            recipe.chefs_kisses.remove(request.user)
        else:
            recipe.chefs_kisses.add(request.user)

        # now want the template to refresh to show the change
        return HttpResponseRedirect(reverse('recipe_details', args=[kwargs['pk']]))


# viewing the users recipes in their ebook
class UsereBookView(generic.ListView):
    model = Recipe
    template_name = "my_ebook.html"

    def get_context_data(self, *args, **kwargs):
        context = super(UsereBookView, self).get_context_data(*args, **kwargs)
        users_recipes = Recipe.objects.filter(chef=self.kwargs['pk'])

        # context['users_recipes'] = users_recipes.values_list()
        context = {
            'users_recipes': users_recipes,
        }
        return context


class MyeBookRecipeSearchView(generic.ListView):
    def get(self, request, *args, **kwargs):

        search_input = request.GET.get('search').replace(" ", "")
        recipes = Recipe.objects.filter(title__icontains=search_input).filter(chef=request.user.id)

        # checking if search isnt blank and if any recipes title contain it
        if search_input != '' and recipes:
            context = {
                'recipes': recipes,
                'num_results': len(recipes)
            }
        else:
            context = {
                'recipes': 'none',
                'num_results': 0,
                'message': "None of your Recipe's titles contain all or part of this search"
            }
        return render(request, 'my_ebook.html', context)
