from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='index'),            # for /form/
    path("contact/", views.contact, name="contact") # for /form/contact/
]
