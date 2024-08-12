""" the url module to define the urls """
from django.urls import path
from . import views
from .views import CustomLoginView, CustomLogoutView, delete_account

app_name = 'core'

urlpatterns = [
        path("", views.index, name="index"),
        path("signin/", CustomLoginView.as_view(), name="login"),
        path("signout/", CustomLogoutView.as_view(), name="logout"),
        path("signup/", views.signup, name="signup"),
        path("about/", views.about, name="about"),
        path("contact/", views.contact, name="contact"),
        path("new_product/", views.new_product, name="new_product"),
        path("edit_product/", views.edit_product, name="edit_product"),
        path("delete_account/", views.delete_account, name="delete_account"),
        ]
