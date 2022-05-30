""" test file for conducting tests on my forms """

from django.test import TestCase
from .forms import CreateRecipeForm, AddIngredientFormSet, AddMethodFormSet


class TestForms(TestCase):
    """
    TestForms class inherits from Django's TestCase
    Contains all my tests on my forms
    """

    def test_title_field_is_required(self):
        """ tests if the title field is required """
        form = CreateRecipeForm(
            {
                'title': ''
            }
        )
        self.assertFalse(form.is_valid())

    def test_chefs_kisses_is_not_required(self):
        """ tests if the chefs_kisses field is not required """
        form = CreateRecipeForm(
            {
                'title': 'recipe1',
                'chefs_kisses': None,
            }
        )
        self.assertTrue(form.is_valid())

    def test_tags_are_not_required(self):
        """ tests if the tags field is not required """
        form = CreateRecipeForm(
            {
                'title': 'recipe1',
                'tags': None,
            }
        )
        self.assertTrue(form.is_valid())

    def test_cover_image_is_not_required(self):
        """ tests if the cover_image field is not required """
        form = CreateRecipeForm(
            {
                'title': 'recipe1',
                'cover_image': None,
            }
        )
        self.assertTrue(form.is_valid())

    def test_ingredients_are_not_required(self):
        """ tests if the ingredients items are not required """
        form = AddIngredientFormSet(
            {
                'items-TOTAL_FORMS': '0',
                'items-INITIAL_FORMS': '0',
                'items-MIN_NUM_FORMS': '0',
                'items-MAX_NUM__FORMS': '1000',
            }
        )
        self.assertTrue(form.is_valid())

    def test_method_setps_are_not_required(self):
        """ tests if the method steps are not required """
        form = AddMethodFormSet(
            {
                'steps-TOTAL_FORMS': '0',
                'steps-INITIAL_FORMS': '0',
                'steps-MIN_NUM_FORMS': '0',
                'steps-MAX_NUM__FORMS': '1000',
            }
        )
        self.assertTrue(form.is_valid())
