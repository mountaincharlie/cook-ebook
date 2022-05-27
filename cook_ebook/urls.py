from . import views
from django.urls import path

urlpatterns = [
    # where 'home' is the name reffered to when creating the link with url
    path('', views.TagList.as_view(), name='home'),
    path('search-recipes/', views.RecipeSearchView.as_view(), name='search_recipes'),
    path('search-tags/<int:pk>', views.RecipeByTagView.as_view(), name='search_tags'),
    path('recipe-details/<int:pk>', views.RecipeDetailsView.as_view(), name='recipe_details'),
    path('recipe-chefs-kiss/<int:pk>', views.RecipeChefsKissView.as_view(), name='recipe_chefs_kiss'),
    path('my-ebook/<str:username>', views.UsereBookView.as_view(), name='my_ebook'),
    path('my-ebook-search-recipes/', views.MyeBookRecipeSearchView.as_view(), name='my_ebook_search_recipes'),
    path('create-recipe/', views.CreateRecipeView.as_view(), name='create_recipe'),
    path('edit-recipe/<int:pk>', views.EditRecipeView.as_view(), name='edit_recipe'),
    path('delete-recipe/<int:pk>', views.DeleteRecipeView.as_view(), name='delete_recipe'),
    path('about/', views.AboutPageView.as_view(), name='about'),
]
