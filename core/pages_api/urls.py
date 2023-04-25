from django.urls import path

from . import views

urlpatterns = [
path('item_list/',views.ListItem.as_view()),
path('item_detail/<int:pk>/',views.ItemDetail.as_view()),
]
