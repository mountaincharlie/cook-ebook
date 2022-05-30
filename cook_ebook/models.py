"""
Django's models.py where I have created the classes
for each of my database tables
"""

import random
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from colorfield.fields import ColorField


# tuple for storing the possible values for a recipe's public_status
PUBLIC_STATUS = ((0, 'Private'), (1, 'Public'), (2, 'Awaits'))


class Tag(models.Model):
    """
    Class for Tag table
    Contains:
    -tag field (label for each tag)
    -color field (unique color for each tag)
    """
    tag = models.CharField(max_length=100)
    color = ColorField(unique=True)

    def __str__(self):
        return str(self.tag)


def random_slug():

    # generate 10 random numbers
    random_numbers_list = [random.randint(0, 100) for i in range(20)]
    # make integer list into string list
    random_str_list = [str(i) for i in random_numbers_list]
    # joining list items into one long string
    random_str = str("".join(random_str_list))

    return random_str


class Recipe(models.Model):
    title = models.CharField(max_length=80)
    summary = models.TextField(max_length=200, blank=True)
    cover_image = CloudinaryField('image', default='placeholder')
    tags = models.ManyToManyField(Tag, blank=True, related_name='recipe_tag')
    public_status = models.IntegerField(choices=PUBLIC_STATUS, default=0)
    created_date = models.DateTimeField(auto_now_add=True)
    chef = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipe_creator')
    slug = models.SlugField(max_length=200, unique=True, default=random_slug)
    chefs_kisses = models.ManyToManyField(User, blank=True, related_name='recipe_chefs_kiss')

    class Meta:
        ordering = ['-created_date']
    
    def __str__(self):
        return self.title
    
    def number_of_chefs_kisses(self):
        return self.chefs_kisses.count()


class Ingredient(models.Model):
    item = models.CharField(max_length=200)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="items", null=True)

    def __str__(self):
        return self.item


class Method(models.Model):
    step = models.CharField(max_length=400)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="steps", null=True)

    def __str__(self):
        return self.step
