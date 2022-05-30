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
    Class for Tag table in the database
    Contains:
    -tag field (label for each tag)
    -color field (unique color for each tag)
    """
    tag = models.CharField(max_length=100)
    color = ColorField(unique=True)

    def __str__(self):
        return str(self.tag)


def random_slug():
    """
    Method for generating a random string of digits.
    Used by the slugField default in the Recipe class.
    This method:
    -generates a list of 20 random integers in the range 0 to 100
    -turns the integer list into a string list
    -joins all the string list items into one string
    -returns the string
    """
    random_numbers_list = [random.randint(0, 100) for i in range(20)]
    random_str_list = [str(i) for i in random_numbers_list]
    random_str = str("".join(random_str_list))

    return random_str


class Recipe(models.Model):
    """
    Creating the Recipe class which inherits Django's models.Model and
    represents the Recipe table in the database
    Contains the fields:
    -title
    -summary
    -cover_image
    -tags (many-to-many relationship)
    -public_status
    -created_date
    -chef (foreign-key relationship)
    -slug
    -chefs_kisses (many-to-many relationship)
    """
    title = models.CharField(max_length=80)
    summary = models.TextField(max_length=200, blank=True)
    cover_image = CloudinaryField('image', default='placeholder')
    tags = models.ManyToManyField(Tag, blank=True, related_name='recipe_tag')
    public_status = models.IntegerField(choices=PUBLIC_STATUS, default=0)
    created_date = models.DateTimeField(auto_now_add=True)
    chef = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='recipe_creator'
    )
    slug = models.SlugField(max_length=200, unique=True, default=random_slug)
    chefs_kisses = models.ManyToManyField(
        User,
        blank=True,
        related_name='recipe_chefs_kiss'
    )

    class Meta:
        """ meta data for how to order recipes """
        ordering = ['-created_date']

    def __str__(self):
        """ method to return the title as a string for each recipe """
        return str(self.title)

    def number_of_chefs_kisses(self):
        """ method for counting the number of chefs_kisses for a recipe """
        return self.chefs_kisses.count()


class Ingredient(models.Model):
    """
    Class for Ingredient table in the database
    Contains:
    -item field (label for each item)
    -recipe (foreign-key relationship)
    """
    item = models.CharField(max_length=200)
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE,
        related_name="items",
        null=True
    )

    def __str__(self):
        """ method to return the item as a string for each ingredient """
        return str(self.item)


class Method(models.Model):
    """
    Class for Method table in the database
    Contains:
    -step field (label for each step)
    -recipe (foreign-key relationship)
    """
    step = models.CharField(max_length=400)
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name="steps",
        null=True
    )

    def __str__(self):
        """ method to return the step as a string for each method step """
        return str(self.step)
