""" test file for conducting tests on my urls """

from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Tag, Recipe


class TestViews(TestCase):
    """
    TestViews class inherits from Django's TestCase
    Contains all the tests I could do for my views
    """

    def test_tags_list_get(self):
        """ tests if the TagList view gets the correct response and uses
        the correct template """
        client = Client()
        response = client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_recipe_search_get(self):
        """ tests if the RecipeSearchView view gets the correct response and
        uses the correct template """
        client = Client()
        data = {'search': 'chicken'}
        response = client.get(reverse('search_recipes'), data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_recipe_by_tag_get(self):
        """ tests if the RecipeByTagView view gets the correct response and
        uses the correct template """
        client = Client()
        Tag.objects.create(
            tag='Chicken',
            color='#ffffff',
        )
        response = client.get(reverse('search_tags', args=['Chicken']))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_recipe_details_get(self):
        """ tests if the RecipeDetailsView view gets the correct response and
        uses the correct template """
        client = Client()
        test_user = User.objects.create_user(username='user1', password='123')
        recipe = Recipe.objects.create(
            title='test_recipe',
            chef=test_user,
            slug=12345678901234567890,
        )
        response = client.get(reverse('recipe_details', args=[recipe.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'recipe_details.html')

    def test_create_recipe_get(self):
        """ tests if the CreateRecipeView view gets the correct response and
        uses the correct template """
        client = Client()
        response = client.get(reverse('create_recipe'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'create_recipe.html')

    def test_about_page(self):
        """ tests if the AboutPageView view gets the correct response and
        uses the correct template """
        client = Client()
        response = client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about.html')
