from django.urls import path

from . import views

urlpatterns = [
   path('', views.inbox, name='inbox'),
   path('new/<int:id>/',views.new_conversation, name='new'),
   path('conversation_detail/<int:id>/', views.conversation_detail,name='conversation_detail'),
]
