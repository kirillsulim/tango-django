from django import forms
from django.contrib.auth.models import User

from rango.models import Category, Page, UserProfile

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


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ["username", "email", "password"]


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ["website", "picture"]

