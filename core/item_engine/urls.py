from django.urls import path
from . import views 

urlpatterns = [
   path('item_detail/<int:id>/', views.item_detail,name='item_detail'), 
   path('add_item/',views.add_item,name="add_item"),
]
