from django.urls import path
from .views import index, add, search


urlpatterns = [
    path("", index),
    path("add_event/", add),
    path("<str:title>/", search)
]
