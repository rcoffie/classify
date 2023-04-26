from django.urls import path

from . import views

urlpatterns = [
    path("item_list/", views.ListItem.as_view()),
    path("category_list/", views.CategoryListView.as_view()),
]
