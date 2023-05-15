from django.urls import path

from . import views

urlpatterns = [
    path('list_item/', views.ListItems.as_view()),
    path('item_details/<int:pk>/',views.ItemDetail.as_view()),
    # path("list_item/", views.ItemListView.as_view()),
    path("update_item/<int:pk>/", views.UpdateItemView.as_view()),
]
