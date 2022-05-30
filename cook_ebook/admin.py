""" Django's admin.py """

from django.contrib import admin
from .models import Recipe, Ingredient, Method, Tag


class IngredientInline(admin.TabularInline):
    """ Tabular inline of the Ingredient table """
    model = Ingredient


class MethodInline(admin.TabularInline):
    """ Tabular inline of the Method table """
    model = Method


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    """
    Admins functionality for Recipes
    The admin can:
    -see the title, public_status, chef and created_data for each recipe
    -search by recipes' title, public_status, created_data and chef username
    -filter recipes by public_status, chef username and created_data
    -execute the make_private, make_public, make_awaits on selected recipes
    -delete any recipes
    """

    list_display = ('title', 'public_status', 'chef', 'created_date')
    search_fields = (
        'title',
        'public_status'
        'created_date',
        'chef__username'
    )
    list_filter = ('public_status', 'chef__username', 'created_date')
    actions = ['make_private', 'make_public', 'make_awaits']

    inlines = [IngredientInline, MethodInline, ]

    def make_private(self, request, queryset):
        """ Changes the public_status of selected recipes to private """
        queryset.update(public_status=0)

    def make_public(self, request, queryset):
        """ Changes the public_status of selected recipes to public """
        queryset.update(public_status=1)

    def make_awaits(self, request, queryset):
        """ Changes the public_status of selected recipes to awaits """
        queryset.update(public_status=2)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    """
    Admins functionality for Tags
    The admin can:
    -see the tag, color, id of any tag
    -search by tags' tag, color, id
    -delete any tags
    """
    list_display = ('tag', 'color', 'id')
    search_fields = ('tag', 'color', 'id')
