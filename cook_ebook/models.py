from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

PUBLIC_STATUS = ((0, 'Private'), (1, 'Public'), (2, 'Awaits'))


class Ingredient(models.Model):
    item = models.CharField(max_length=200)

    def __str__(self):
        return self.item


class Method(models.Model):
    step = models.CharField(max_length=400)

    def __str__(self):
        return self.step


class Tag(models.Model):
    tag = models.CharField(max_length=100)

    def __str__(self):
        return self.tag


class Recipe(models.Model):
    title = models.CharField(max_length=150)
    summary = models.TextField(blank=True)
    cover_image = CloudinaryField('image', default='placecholder')
    ingredients = models.ManyToManyField(Ingredient, related_name='recipe_item')
    method = models.ManyToManyField(Method, related_name='recipe_step')
    tags = models.ManyToManyField(Tag, blank=True, related_name='recipe_tag')
    public_status = models.IntegerField(choices=PUBLIC_STATUS, default=0)
    created_date = models.DateTimeField(auto_now_add=True)
    chef = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipe_creator')
    slug = models.SlugField(max_length=150, unique=True)
    chefs_kisses = models.ManyToManyField(User, blank=True, related_name='recipe_chefs_kiss')

    class Meta:
        ordering = ['-created_date']
    
    def __str__(self):
        return self.title
    
    def number_of_chefs_kisses(self):
        return self.chefs_kisses.count()
