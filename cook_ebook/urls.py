from . import views
from django.urls import path

urlpatterns = [
    # where 'home' is the name reffered to when creating the link with url
    path('', views.TagList.as_view(), name='home'),
    path('search-recipes/', views.RecipeSearchView.as_view(), name='search_recipes'),
    path('search-tags/<int:pk>', views.RecipeByTagView.as_view(), name='search_tags'),
    path('recipe-details/<int:pk>', views.RecipeDetailsView.as_view(), name='recipe_details'),
    path('recipe-chefs-kiss/<int:pk>', views.RecipeChefsKissView.as_view(), name='recipe_chefs_kiss'),
]
