from django.contrib import admin
from .models import Recipe, Ingredient, Method, Tag

admin.site.register(Recipe)
admin.site.register(Ingredient)
admin.site.register(Method)
admin.site.register(Tag)
