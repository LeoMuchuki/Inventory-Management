""" This module defines how the forms will look like """
from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field, HTML
from django.contrib.auth import get_user_model

user = get_user_model()


class NewProduct(forms.Form):
    """ a form to add a new product. """
    name = forms.CharField(label="Name of the product", max_length=100)
    prod_type = forms.CharField(label="Type of the product", max_length=100)
    sku = forms.CharField(label="unique sku", max_length=20)
    description = forms.CharField(label="description", max_length=200)
    price = forms.IntegerField


class EditProduct(forms.Form):
    """ a form to edit an existing product. """
    name = forms.CharField(label="Name of the product", max_length=100)
    prod_type = forms.CharField(label="Type of the product", max_length=100)
    description = forms.CharField(label="description", max_length=200)
    price = forms.IntegerField

class LoginForm(AuthenticationForm):
    username = forms.EmailField(
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Email",
                "class": "form-control",
            }
        ),
    )
    password = forms.CharField(
        max_length=50,
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control",
                "data-toggle": "password",
                "id": "password",
                "name": "password",
            }
        ),
    )

    class Meta:
        model = user
        fields = ["email", "password"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
                'username',
                Field('password', css_class='form-control'),
                HTML("""
                <label>
                    <input type="checkbox" onclick="togglePasswordVisibility()"> Show Password
                </label>
                """),
                Submit('submit', 'login')
                )




class SignUpForm(UserCreationForm):
    first_name = forms.CharField(
            max_length=50,
            required=True,
            widget=forms.TextInput(
                attrs={
                    "placeholder": "First Name"
                    }))
    last_name = forms.CharField(
            max_length=50,
            required=True,
            widget=forms.TextInput(
                attrs={
                    "placeholder": "Last Name"
                    }))
    email = forms.EmailField(
        max_length=100,
        required=True,
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Email",
                "class": "form-control",
            }
        ),
    )

    password1 = forms.CharField(
        max_length=50,
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control",
                "data-toggle": "password",
                "id": "password1",
                "name": "password1",
                "minlength": "3"
            }
        ),
    )
    password2 = forms.CharField(
        max_length=50,
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "confirm Password",
                "class": "form-control",
                "data-toggle": "password",
                "id": "password2",
                "name": "password2",
                "minlength": "3"
            }
        ),
    )

    class Meta:
        model = user
        fields = ["first_name", "last_name", "email", "password1", "password2"]

# CustomUserChangeForm for admin user change
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = user
        fields = ['email', 'first_name', 'last_name', 'is_active', 'is_staff']

# CustomUserCreationForm for admin user creation
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = user
        fields = ['email', 'first_name', 'last_name', 'password1', 'password2']
