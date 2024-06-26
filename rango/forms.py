from django import forms
from rango.models import Category, Page


class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text="Enter category name")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.IntegerField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Category
        fields = ("name", )


class PageForm(forms.ModelForm):
    title = forms.CharField(max_length=128, help_text="Enter page title")
    url = forms.URLField(max_length=200, help_text="Enter Url")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        model = Page
        exclude = ("category", )


