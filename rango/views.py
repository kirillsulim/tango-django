from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

from rango.models import Page, Category
from rango.forms import CategoryForm, PageForm


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


def add_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print(form.errors)
    else:
        form = CategoryForm()

    return render(request, "rango/add_category.html", {"form": form})


def add_page(request, category_name_slug):
    try:
        cat = Category.objects.get(slug=category_name_slug)
    except Category.DoesNotExist:
        cat = None

    if request.method == "POST":
        form = PageForm(request.POST)
        if form.is_valid():
            if cat:
                page = form.save(commit=False)
                page.category = cat
                page.save()

                return category(request, category_name_slug)
            else:
                return index(request)
        else:
            print(form.errors)
    else:
        form = PageForm()

    return render(request, "rango/add_page.html", {"form": form, "category": cat, })

