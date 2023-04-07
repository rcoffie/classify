from django.urls import path

from . import views

urlpatterns = [
    path("item_detail/<int:id>/", views.item_detail, name="item_detail"),
    path("add_item/", views.add_item, name="add_item"),
    path("edit_item/<int:id>/", views.edit_item, name="edit_item"),
    path("delete_item/<int:id>/", views.delete_item, name="delete_item"),
    path("item_list/", views.item_list, name="item_list"),
]
