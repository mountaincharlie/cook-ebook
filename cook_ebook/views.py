"""
Django's views.py where I have created the class based views
which control the data that is displayed and gathered between each
of the templates and the database, through the urls.
"""

from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Tag, Recipe, Ingredient, Method
from .forms import CreateRecipeForm, AddIngredientFormSet, AddMethodFormSet


class TagList(generic.ListView):
    """
    TagList class based view inheriting Django's generic.ListView
    Uses the Tag model for viewing the tags on the homepage.
    Obtains all of the objects in Tag and stores it in queryset, to
    be used in index.html as 'tag_list'.
    Used in the index.html template
    """
    model = Tag
    queryset = Tag.objects.all()
    template_name = "index.html"


class RecipeSearchView(generic.ListView):
    """
    RecipeSearchView class based view inheriting Django's generic.ListView
    Contains the get method for displaying search results from searches by
    recipe title.
    """

    def get(self, request, *args, **kwargs):
        """
        get method for when users submit the search by recipe title form on
        the homepage.
        -takes the search_input (removing any blank spaces incase of user
        error)
        -filters through all of the Recipe objects using title__icontains for
        the search_input and public_status=1 (since only public recipes can
        be viewed outside a user's My eBook page)
        -checks if the search is not blank at that at least one recipe was
        found and adds these recipes and the length of results into the
        context var
        -else it adds that there were no results and a message to the user
        into the context var
        -returns rendering index.html with the request and context data
        """
        search_input = request.GET.get('search').replace(" ", "")
        recipes = Recipe.objects.filter(
            title__icontains=search_input
        ).filter(
            public_status=1
        )

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
    """
    RecipeByTagView class based view inheriting Django's generic.ListView
    Contains the get method for displaying search results from searches by
    tag tile.
    """

    def get(self, request, *args, **kwargs):
        """
        get method for when users click on a tag tile to see the recipes
        containing that tag.
        -finds the chosen_tag by its tag which is passed through the url
        -filters through all of the Recipe objects using the id of the
        chosen_tag and public_status=1 (since only public recipes can
        be viewed outside a user's My eBook page)
        -checks if at least one recipe was found and adds these recipes
        and the length of results into the context var
        -else it adds that there were no results and a message to the user
        into the context var
        -returns rendering index.html with the request and context data
        """
        chosen_tag = get_object_or_404(Tag, tag=self.kwargs['tag'])
        recipes = Recipe.objects.filter(
            tags=chosen_tag.id
        ).filter(
            public_status=1
        )

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
    """
    RecipeDetailsView class based view inheriting Django's View
    Contains the get method for displaying the details for a chosen
    recipe.
    """

    def get(self, request, *args, **kwargs):
        """
        get method for when users click on a recipe card to see the recipe's
        full details.
        -gets all of the Recipe objects
        -gets the sepcific chosen recipe by its unique slug
        -gets all the ingredient items by the recipe
        -gets all the method steps by the recipe
        -sets a chefs_kiss variable as False
        -checks if the current user has left a chefs kiss on this recipe
        -if so, it sets chefs_kiss as True
        -sets context dict with the recipe, its ingredients, its method
        and its chefs_kiss status
        -returns rendering recipe_details.html with the request and context
        data
        """
        recipes = Recipe.objects.all()
        recipe = get_object_or_404(recipes, slug=self.kwargs['slug'])

        ingredients = Ingredient.objects.filter(recipe=recipe)
        method = Method.objects.filter(recipe=recipe)

        chefs_kiss = False
        if recipe.chefs_kisses.filter(id=self.request.user.id).exists():
            chefs_kiss = True

        context = {
            'recipe': recipe,
            'ingredients': ingredients,
            'method': method,
            'chefs_kiss': chefs_kiss,
        }

        return render(request, 'recipe_details.html', context)


class RecipeChefsKissView(View):
    """
    RecipeChefsKissView class based view inheriting Django's View
    Contains the post method for changing the chefs kiss icon and
    chefs_kisses count in the recipe's recipe_details page when the
    user clicks the chefs kiss button.
    """

    def post(self, request, *args, **kwargs):
        """
        post method for when users click on recipe's chefs kiss button.
        -gets the recipe by its unique slug
        -if statement for finding if the user's id already exists for
        this recipe's chefs_kisses field
        -if the user exists then it removes the user
        -else it adds the user
        -returns HttpResponseRedirect to reverse recipe_details url to
        show the change
        """
        recipe = get_object_or_404(Recipe, slug=self.kwargs['slug'])

        if recipe.chefs_kisses.filter(id=request.user.id).exists():
            recipe.chefs_kisses.remove(request.user)
        else:
            recipe.chefs_kisses.add(request.user)

        return HttpResponseRedirect(
            reverse('recipe_details', args=[kwargs['slug']])
        )


class UsereBookView(generic.ListView):
    """
    UsereBookView class based view inheriting Django's generic.ListView
    Uses the Recipe model for viewing the user's recipes on their My eBook
    page, which uses the my_ebook.html template
    Contains the get_context_data method for getting the user's recipes.
    """
    model = Recipe
    template_name = "my_ebook.html"

    def get_context_data(self, *args, **kwargs):
        """
        get_context_data method for displaying the user's recipes on their
        My eBook page.
        -sets up the get_context_data method on the Class itself
        -gets the current user by their username which is passed into
        the view through the url
        -gets the user's recipes by the user's id
        -gets all of the Tag objects
        -passes the users recipes, the current user (as 'authorised_user')
        and all of the tags into the context var
        -returns context
        """
        context = super(UsereBookView, self).get_context_data(*args, **kwargs)
        current_user = User.objects.filter(username=self.kwargs['username'])
        users_recipes = Recipe.objects.filter(chef=current_user[0].id)
        all_tags = Tag.objects.all()

        context = {
            'users_recipes': users_recipes,
            'authorised_user': current_user[0].username,
            'all_tags': all_tags,
        }
        return context


class MyeBookRecipeSearchView(generic.ListView):
    """
    MyeBookRecipeSearchView class based view inheriting Django's
    generic.ListView
    Contains the get method for displaying search results from searches by
    recipe title within the users My eBook page.
    """
    def get(self, request, *args, **kwargs):
        """
        get method for when users submit the search by recipe title form on
        their My eBook page.
        -takes the search_input (removing any blank spaces incase of user
        error)
        -filters through all of the Recipe objects using title__icontains for
        the search_input and chef= the user's id (only the user's recipes can
        be viewed on their My eBook page)
        -checks if the search is not blank at that at least one recipe was
        found and adds these recipes, the length of results and the current
        user as the 'authorised_user' into the context var
        -else it adds that there were no results, a message to the user and
        the current user as the 'authorised_user' into the context var
        -returns rendering my_ebook.html with the request and context data
        """
        search_input = request.GET.get('search').replace(" ", "")
        recipes = Recipe.objects.filter(
            title__icontains=search_input
        ).filter(
            chef=request.user.id
        )

        if search_input != '' and recipes:
            context = {
                'recipes': recipes,
                'num_results': len(recipes),
                'authorised_user': request.user.username,
            }
        else:
            context = {
                'recipes': 'none',
                'num_results': 0,
                'message': "None of your Recipe's titles contain all or part of this search",
                'authorised_user': request.user.username,
            }
        return render(request, 'my_ebook.html', context)


class MyeBookTagSearchView(generic.ListView):
    """
    MyeBookTagSearchView class based view inheriting Django's
    generic.ListView
    Contains the get method for displaying search results from searches by
    tag tile in the user's My eBook.
    """
    def get(self, request, *args, **kwargs):
        """
        get method for when users click on a tag tile to see the recipes
        containing that tag.
        -finds the chosen_tag by its tag which is passed through the url
        -filters through all of the Recipe objects using the id of the
        chosen_tag and chef= user's id (since only the user's recipes can
        be viewed in their My eBook page)
        -checks if the search is not blank at that at least one recipe was
        found and adds these recipes, the length of results and the current
        user as the 'authorised_user' into the context var
        -else it adds that there were no results, a message to the user and
        the current user as the 'authorised_user' into the context var
        -returns rendering my_ebook.html with the request and context data
        """
        chosen_tag = get_object_or_404(Tag, tag=self.kwargs['tag'])
        recipes = Recipe.objects.filter(
            tags=chosen_tag.id
        ).filter(
            chef=request.user.id
        )

        if len(recipes) != 0:
            context = {
                'recipes': recipes,
                'num_results': len(recipes),
                'authorised_user': request.user.username,
            }
        else:
            context = {
                'recipes': 'none',
                'num_results': len(recipes),
                'message': 'None of your recipes have been assigned this tag yet',
                'authorised_user': request.user.username,
            }
        return render(request, 'my_ebook.html', context)


class CreateRecipeView(View):
    """
    CreateRecipeView class based view inheriting Django's View
    Contains the get method for displaying the forms to create a recipe
    in the Create Recipe page.
    Contains the post method for taking in the data submitted in the Create
    Recipe forms.
    """

    def get(self, request, *args, **kwargs):
        """
        get method for getting the forms to be displayed to the user.
        -gets the CreateRecipeForm() form
        -gets the AddIngredientFormSet() formset
        -gets the AddMethodFormSet() formset
        -passes these into the context var
        -returns rendering create_recipe.html with the request and context data
        """

        recipe_form = CreateRecipeForm()
        ingredients_formset = AddIngredientFormSet()
        method_formset = AddMethodFormSet()

        context = {
            'recipe_form': recipe_form,
            'ingredients_formset': ingredients_formset,
            'method_formset': method_formset,
        }

        return render(request, 'create_recipe.html', context)

    def post(self, request, *args, **kwargs):
        """
        post method for when users click on the Create button, which
        submits the create recipe forms.
        -gets the CreateRecipeForm populated with data via request.POST
        and request.FILES
        -checks that the form is valid and if not, it returns the
        CreateRecipeForm again for the user to correct the invalid form
        fields
        -if its valid:
        -it saves the form as 'recipe' without commiting
        it yet.
        -sets the current user as the 'chef'
        -uses request.FILES.get method to set the upload_image as 'cover_image'
        -uses the request.POST.getlist method to get all of the tags with
        checked checkboxes and saves this all
        -gets the AddIngredientFormSet populated with data via request.POST
        and with the recipe as its 'instance'
        -if the formset is valid its saved
        -gets the AddMethodFormSet populated with data via request.POST
        and with the recipe as its 'instance'
        -if the formset is valid its saved
        -a custom success message is passed into django messages.success along
        with request
        -the user is then redirected to their My eBook page
        """

        recipe_form = CreateRecipeForm(request.POST, request.FILES)

        if recipe_form.is_valid():
            recipe = recipe_form.save(commit=False)
            recipe.chef = User.objects.get(id=self.request.user.id)
            recipe.cover_image = request.FILES.get('upload_image')
            recipe.save()
            checked_tags = request.POST.getlist('tags')
            recipe.tags.set(checked_tags)
            recipe.save()

            ingredients_formset = AddIngredientFormSet(
                request.POST, instance=recipe
            )

            if ingredients_formset.is_valid():
                ingredients_formset.save()

                method_formset = AddMethodFormSet(
                    request.POST, instance=recipe
                )

                if method_formset.is_valid():
                    method_formset.save()

            messages.success(
                request,
                ('Your recipe was successfully created!')
            )
            return redirect(f'/my-ebook/{self.request.user.username}')
        else:
            context = {
                'recipe_form': recipe_form,
            }
            return render(request, 'create_recipe.html', context)


class EditRecipeView(View):
    """
    EditRecipeView class based view inheriting Django's View
    Contains the get method for displaying the forms to edit a recipe
    in the Edit Recipe page, populated with the recipes current data.
    Contains the post method for taking in the data submitted in the Edit
    Recipe forms and updating the recipe.
    """

    def get(self, request, *args, **kwargs):
        """
        get method for getting the forms to be displayed to the user.
        -gets the recipe by its unique slug
        -gets the CreateRecipeForm() form with instance = the recipe
        -gets the AddIngredientFormSet() formset instance = the recipe
        -gets the AddMethodFormSet() formset instance = the recipe
        -passes these into the context var
        -returns rendering edit_recipe.html with the request and context data
        """
        recipe = get_object_or_404(Recipe, slug=self.kwargs['slug'])

        recipe_form = CreateRecipeForm(instance=recipe)
        ingredients_formset = AddIngredientFormSet(instance=recipe)
        method_formset = AddMethodFormSet(instance=recipe)

        context = {
            'recipe': recipe,
            'recipe_form': recipe_form,
            'ingredients_formset': ingredients_formset,
            'method_formset': method_formset,
        }

        return render(request, 'edit_recipe.html', context)

    def post(self, request, *args, **kwargs):
        """
        post method for when users click on the Edit button, which
        submits the recipe forms.
        -gets the recipe by its unique slug
        -gets the CreateRecipeForm populated with data via request.POST
        and request.FILES and with instance = the recipe
        -checks that the form is valid and if not, it returns the
        CreateRecipeForm again for the user to correct the invalid form
        fields
        -if its valid:
        -it saves the form without commiting it yet
        -sets the current user as the 'chef'
        -checks if a new image was uploaded, else it keps the original as
        cover_image (since the ImageField doesn't show the chosen image in
        the edit page)
        -uses the request.POST.getlist method to get all of the tags with
        checked checkboxes and saves this all
        -gets the AddIngredientFormSet populated with data via request.POST
        and with the recipe as its 'instance'
        -if the formset is valid its saved
        -gets the AddMethodFormSet populated with data via request.POST
        and with the recipe as its 'instance'
        -if the formset is valid its saved
        -a custom success message is passed into django messages.success along
        with request
        -the user is then redirected to their My eBook page
        """
        recipe = get_object_or_404(Recipe, slug=self.kwargs['slug'])

        recipe_form = CreateRecipeForm(
            request.POST,
            request.FILES,
            instance=recipe
        )

        if recipe_form.is_valid():
            recipe = recipe_form.save(commit=False)
            recipe.chef = User.objects.get(id=self.request.user.id)
            if request.FILES.get('upload_image'):
                recipe.cover_image = request.FILES.get('upload_image')
                recipe.save()
            checked_tags = request.POST.getlist('tags')
            recipe.tags.set(checked_tags)
            recipe.save()

            ingredients_formset = AddIngredientFormSet(
                request.POST,
                instance=recipe
            )

            if ingredients_formset.is_valid():
                ingredients_formset.save()

                method_formset = AddMethodFormSet(
                    request.POST,
                    instance=recipe
                )

                if method_formset.is_valid():
                    method_formset.save()

            messages.success(
                request,
                ('Your recipe was successfully updated!')
            )
            return redirect(f'/my-ebook/{self.request.user.username}')
        else:
            context = {
                'recipe_form': recipe_form,
            }
            return render(request, 'edit_recipe.html', context)


class DeleteRecipeView(generic.DeleteView):
    """
    DeleteRecipeView class based view inheriting Django's
    generic.DeleteView
    Uses the Recipe model and delete_recipe.html template.
    Contains the post method for taking the recipe that the user confirms
    they want to delete and deletes it from the database.
    """
    model = Recipe
    template_name = "delete_recipe.html"

    def post(self, request, *args, **kwargs):
        """
        post method for when users click on the Delete button in the Delete
        Recipe page, which is for confirming the user wants to delete the
        recipe.
        -gets the recipe by its unique slug
        -deletes the recipe from the database
        -a custom success message is passed into django messages.success along
        with request
        -the user is then redirected to their My eBook page
        """
        recipe = get_object_or_404(Recipe, slug=self.kwargs['slug'])

        recipe.delete()

        messages.success(request, ('Your recipe was successfully deleted!'))
        return redirect(f'/my-ebook/{self.request.user.username}')


class AboutPageView(generic.ListView):
    """
    AboutPageView class based view inheriting Django's generic.ListView
    Uses the User model so that the is_authenticated ethod can be used to
    check if the user is logged in (for whether or not the 'Give Feedback'
    section can be displayed).
    Used in the about.html template
    """
    model = User
    template_name = "about.html"
