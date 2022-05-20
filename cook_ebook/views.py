from django.shortcuts import render
from django.views import generic, View
from .models import Tag, Recipe


# viewing the recipes on the homepage
class TagList(generic.ListView):
    # table model to use
    model = Tag
    queryset = Tag.objects.all()
    # the template to show the list in (as 'tag_list')
    template_name = "index.html"


class RecipeSearchView(generic.ListView):

    def get(self, request, *args, **kwargs):

        queryset = Recipe.objects.all()
        search_input = request.GET.get('search').replace(" ", "")
        recipes = Recipe.objects.filter(title__icontains=search_input).filter(public_status=1)

        # checking if search isnt blank and if any of recipes exits in queryset
        if search_input != '' and bool(set(recipes) & set(queryset)):
            context = {
                'recipes': recipes,
                'num_results': len(recipes)
            }
        else:
            # print(recipes)
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
