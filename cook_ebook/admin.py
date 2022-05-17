from django.contrib import admin
from .models import Recipe, Ingredient, Method, Tag

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):

    list_display = ('title', 'public_status', 'chef', 'created_date')
    search_fields = ('title', 'public_status', 'created_date', 'chef__username')
    list_filter = ('public_status', 'chef__username', 'created_date')
    actions = ['make_private', 'make_public', 'make_awaits']

    # changes status to private
    def make_private(self, request, queryset):
        queryset.update(public_status=0)

    # changes status to public
    def make_public(self, request, queryset):
        queryset.update(public_status=1)

    # changes status to awaits
    def make_awaits(self, request, queryset):
        queryset.update(public_status=2)


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('item', 'id')
    search_fields = ('item', 'id')


admin.site.register(Method)
admin.site.register(Tag)
