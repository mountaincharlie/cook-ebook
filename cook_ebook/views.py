from django.shortcuts import render
from django.views import generic, View
from .models import Tag


# viewing the recipes on the homepage
class TagList(generic.ListView):
    # table model to use
    model = Tag
    # the template to show the list in (as 'tag_list')
    template_name = "index.html"
