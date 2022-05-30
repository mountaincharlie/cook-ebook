""" test file for conducting tests on my models """

from django.test import TestCase
from django.contrib.auth.models import User
from django.db import IntegrityError
from .models import Recipe, Tag, Ingredient, Method


class TestModels(TestCase):
    """
    TestModels class inherits from Django's TestCase
    Contains all my tests on my models
    """

    def test_recipes_private_by_default(self):
        """ tests if recipes are created as private by default """
        test_user = User.objects.create_user(username='user1', password='123')
        recipe = Recipe.objects.create(
            title='test_recipe',
            chef=test_user,
        )
        self.assertEqual(recipe.public_status, 0)

    def test_number_of_chefs_kisses_method(self):
        """ tests if the number_of_chefs_kisses method works correctly """
        test_user = User.objects.create_user(username='user1', password='123')
        test_user2 = User.objects.create_user(username='user2', password='123')
        recipe = Recipe.objects.create(
            title='test_recipe',
            chef=test_user,
        )
        recipe.chefs_kisses.set([test_user, test_user2])
        self.assertEqual(recipe.number_of_chefs_kisses(), 2)

    def test_tag_color_must_be_unique(self):
        """ tests if tag colors must be unique """
        with self.assertRaises(IntegrityError) as context:
            Tag.objects.create(
                tag='tag1',
                color='#ffffff',
            )
            Tag.objects.create(
                tag='tag2',
                color='#ffffff',
            )
        self.assertTrue('UNIQUE constraint failed' in str(context.exception))

    def test_slugs_must_be_unique(self):
        """ tests if recipe's slugs must be unique """
        with self.assertRaises(IntegrityError) as context:
            test_user = User.objects.create_user(
                username='user1',
                password='123'
            )
            test_user2 = User.objects.create_user(
                username='user2',
                password='123'
            )
            Recipe.objects.create(
                title='title1',
                chef=test_user,
                slug='a-slug',
            )
            Recipe.objects.create(
                title='title2',
                chef=test_user2,
                slug='a-slug',
            )
        self.assertTrue('UNIQUE constraint failed' in str(context.exception))

    def test_random_slug_function_generates_random_str(self):
        """ tests if the random_slug method generates random, unique slugs """
        test_user = User.objects.create_user(username='user1', password='123')
        test_user2 = User.objects.create_user(username='user2', password='123')
        recipe1 = Recipe.objects.create(
            title='title1',
            chef=test_user,
        )
        recipe2 = Recipe.objects.create(
            title='title2',
            chef=test_user2,
        )
        self.assertFalse(recipe1.slug == recipe2.slug)

    def test_tag_string_method_returns_tag(self):
        """ tests if the tag model's str method returns tag as a string """
        tag = Tag.objects.create(tag='Chicken')
        self.assertEqual(str(tag), 'Chicken')

    def test_recipe_string_method_returns_title(self):
        """ tests if the recipe model's str method returns title as a
        string """
        test_user = User.objects.create_user(username='user1', password='123')
        recipe = Recipe.objects.create(title='Test Recipe', chef=test_user)
        self.assertEqual(str(recipe), 'Test Recipe')

    def test_ingredient_string_method_returns_item(self):
        """ tests if the ingredient model's str method returns item as a
        string """
        item = Ingredient.objects.create(item='Pasta')
        self.assertEqual(str(item), 'Pasta')

    def test_method_string_method_returns_step(self):
        """ tests if the method model's str method returns step as a string """
        step = Method.objects.create(step='Boil the pasta.')
        self.assertEqual(str(step), 'Boil the pasta.')
