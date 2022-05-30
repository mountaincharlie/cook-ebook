""" test file for conducting tests on my urls """

from django.test import TestCase
from django.urls import reverse, resolve
from cook_ebook import views


class TestUrls(TestCase):
    """
    TestUrls class inherits from Django's TestCase
    Contains all my tests on my urls
    """

    def test_home_url_resolves(self):
        """ tests if the home url resolves """
        url = reverse('home')
        self.assertEqual(resolve(url).func.view_class, views.TagList)

    def test_search_recipes_url_resolves(self):
        """ tests if the search_recipes url resolves """
        url = reverse('search_recipes')
        self.assertEqual(resolve(url).func.view_class, views.RecipeSearchView)

    def test_search_tags_url_resolves(self):
        """ tests if the search_tags url resolves """
        url = reverse('search_tags', args=['tag-name'])
        self.assertEqual(resolve(url).func.view_class, views.RecipeByTagView)

    def test_recipe_details_url_resolves(self):
        """ tests if the recipe_details url resolves """
        url = reverse('recipe_details', args=[12345678901234567890])
        self.assertEqual(resolve(url).func.view_class, views.RecipeDetailsView)

    def test_recipe_chefs_kiss_url_resolves(self):
        """ tests if the chefs_kiss url resolves """
        url = reverse('recipe_chefs_kiss', args=[12345678901234567890])
        self.assertEqual(
            resolve(url).func.view_class,
            views.RecipeChefsKissView
        )

    def test_my_ebook_url_resolves(self):
        """ tests if the my_ebook url resolves """
        url = reverse('my_ebook', args=['username'])
        self.assertEqual(resolve(url).func.view_class, views.UsereBookView)

    def test_my_ebook_search_recipes_url_resolves(self):
        """ tests if the my_ebook_search url resolves """
        url = reverse('my_ebook_search_recipes')
        self.assertEqual(
            resolve(url).func.view_class,
            views.MyeBookRecipeSearchView
        )

    def test_ebook_search_tags_url_resolves(self):
        """ tests if the ebook_search_tags url resolves """
        url = reverse('ebook_search_tags', args=['tag-name'])
        self.assertEqual(
            resolve(url).func.view_class,
            views.MyeBookTagSearchView
        )

    def test_create_recipe_url_resolves(self):
        """ tests if the create_recipe url resolves """
        url = reverse('create_recipe')
        self.assertEqual(resolve(url).func.view_class, views.CreateRecipeView)

    def test_edit_recipe_url_resolves(self):
        """ tests if the edit_recipe url resolves """
        url = reverse('edit_recipe', args=[12345678901234567890])
        self.assertEqual(resolve(url).func.view_class, views.EditRecipeView)

    def test_delete_recipe_url_resolves(self):
        """ tests if the delete_recipe url resolves """
        url = reverse('delete_recipe', args=[12345678901234567890])
        self.assertEqual(resolve(url).func.view_class, views.DeleteRecipeView)

    def test_about_url_resolves(self):
        """ tests if the about url resolves """
        url = reverse('about')
        self.assertEqual(resolve(url).func.view_class, views.AboutPageView)
