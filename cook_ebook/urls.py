""" Django's urls.py for specifying the url paths for each of
my class based views in views.py """
from django.urls import path
from . import views

urlpatterns = [
    path('', views.TagList.as_view(), name='home'),
    path(
        'search-recipes/',
        views.RecipeSearchView.as_view(),
        name='search_recipes'
        ),
    path(
        'search-tags/<str:tag>',
        views.RecipeByTagView.as_view(),
        name='search_tags'
        ),
    path(
        'recipe-details/<slug:slug>',
        views.RecipeDetailsView.as_view(),
        name='recipe_details'
        ),
    path(
        'recipe-chefs-kiss/<slug:slug>',
        views.RecipeChefsKissView.as_view(),
        name='recipe_chefs_kiss'
        ),
    path(
        'my-ebook/<str:username>',
        views.UsereBookView.as_view(),
        name='my_ebook'
        ),
    path(
        'my-ebook-search-recipes/',
        views.MyeBookRecipeSearchView.as_view(),
        name='my_ebook_search_recipes'
        ),
    path(
        'my-ebook-tags-search/<str:tag>',
        views.MyeBookTagSearchView.as_view(),
        name='ebook_search_tags'
        ),
    path(
        'create-recipe/',
        views.CreateRecipeView.as_view(),
        name='create_recipe'
        ),
    path(
        'edit-recipe/<slug:slug>',
        views.EditRecipeView.as_view(),
        name='edit_recipe'
        ),
    path(
        'delete-recipe/<slug:slug>',
        views.DeleteRecipeView.as_view(),
        name='delete_recipe'
        ),
    path(
        'about/',
        views.AboutPageView.as_view(),
        name='about'
        ),
]
