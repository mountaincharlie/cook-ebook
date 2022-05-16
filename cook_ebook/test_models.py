from django.test import TestCase
from django.contrib.auth.models import User
from .models import Recipe

class TestModels(TestCase):

    def test_recipes_private_by_default(self):
        test_user = User.objects.create_user(username='user1', password='123')
        recipe = Recipe.objects.create(
            title = 'test_recipe',
            chef = test_user,
        )
        self.assertEqual(recipe.public_status, 0)
    

    def test_number_of_chefs_kisses_method(self):
        test_user = User.objects.create_user(username='user1', password='123')
        test_user2 = User.objects.create_user(username='user2', password='123')
        recipe = Recipe.objects.create(
            title = 'test_recipe',
            chef = test_user,
        )
        recipe.chefs_kisses.set([test_user, test_user2])
        self.assertEqual(recipe.number_of_chefs_kisses(), 2)
