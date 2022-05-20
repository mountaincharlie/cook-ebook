from . import views
from django.urls import path

urlpatterns = [
    # where 'home' is the name reffered to when creating the link with url
    path('', views.TagList.as_view(), name='home'),
    path('search-recipes/', views.RecipeSearchView.as_view(), name='search_recipes'),
    path('search-tags/<int:pk>', views.RecipeByTagView.as_view(), name='search_tags'),
    
]
