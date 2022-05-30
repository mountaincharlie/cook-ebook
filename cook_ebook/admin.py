from django.contrib import admin
from .models import Recipe, Ingredient, Method, Tag


class IngredientInline(admin.TabularInline):
    model = Ingredient


class MethodInline(admin.TabularInline):
    model = Method


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):

    list_display = ('title', 'public_status', 'chef', 'created_date')
    search_fields = ('title', 'public_status', 'created_date', 'chef__username')
    list_filter = ('public_status', 'chef__username', 'created_date')
    actions = ['make_private', 'make_public', 'make_awaits']

    inlines = [IngredientInline, MethodInline, ]

    # changes status to private
    def make_private(self, queryset):
        queryset.update(public_status=0)  #  request,

    # changes status to public
    def make_public(self, queryset):
        queryset.update(public_status=1)

    # changes status to awaits
    def make_awaits(self, queryset):
        queryset.update(public_status=2)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('tag', 'color', 'id')
    search_fields = ('tag', 'color', 'id')
