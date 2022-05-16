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
