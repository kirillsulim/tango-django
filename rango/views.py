from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

from rango.models import Page

from rango.models import Category

def index(request):
    category_list_likes = Category.objects.order_by("-likes")[:5]
    category_list_views = Category.objects.order_by("-views")[:5]
    context_dict = {
        "categories_likes": category_list_likes,
        "categories_views": category_list_views,
    }
    return render(request, 'rango/index.html', context_dict)

def category(request, category_name_slug):
    context_dict = {}

    try:
        category = Category.objects.get(slug=category_name_slug)
        context_dict["category_name"] = category.name

        pages = Page.objects.filter(category=category)
        context_dict["pages"] = pages

        context_dict["category"] = category  # For client know that category exists
    except Category.DoesNotExist:
        pass  # no need to do smth

    return render(request, 'rango/category.html', context_dict)

def about(request):
    return  render(request, 'rango/about.html')
