from django.test import TestCase
from .forms import CreateRecipeForm, AddIngredientFormSet, AddMethodFormSet


class TestForms(TestCase):

    def test_title_field_is_required(self):
        form = CreateRecipeForm(
            {
                'title': ''
            }
        )
        self.assertFalse(form.is_valid())

    def test_chefs_kisses_is_not_required(self):
        form = CreateRecipeForm(
            {
                'title': 'recipe1',
                'chefs_kisses': None,
            }
        )
        self.assertTrue(form.is_valid())

    def test_tags_are_not_required(self):
        form = CreateRecipeForm(
            {
                'title': 'recipe1',
                'tags': None,
            }
        )
        self.assertTrue(form.is_valid())

    def test_cover_image_is_not_required(self):
        form = CreateRecipeForm(
            {
                'title': 'recipe1',
                'cover_image': None,
            }
        )
        self.assertTrue(form.is_valid())

    def test_ingredients_are_not_required(self):
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
        form = AddMethodFormSet(
            {
                'steps-TOTAL_FORMS': '0',
                'steps-INITIAL_FORMS': '0',
                'steps-MIN_NUM_FORMS': '0',
                'steps-MAX_NUM__FORMS': '1000',
            }
        )
        self.assertTrue(form.is_valid())
