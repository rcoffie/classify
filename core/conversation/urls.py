from django.urls import path

from . import views

urlpatterns = [
   path('new/<int:id>/',views.new_conversation, name='new'),
]
