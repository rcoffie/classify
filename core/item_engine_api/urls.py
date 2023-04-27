from django.urls import path

from . import views

urlpatterns = [
    path("list_item/", views.ItemListView.as_view()),
    path("item_detail/<int:pk>/", views.ItemDetailView.as_view()),
]
