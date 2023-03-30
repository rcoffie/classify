from django.shortcuts import render
from item_engine.models import Category, Item
# Create your views here.


def home(request):
    items = Item.objects.filter(is_sold=False)[0:3]
    categories = Category.objects.all()
    context = {
        'items':items, 
        'categories':categories,
        }
    return render(request, "pages/home.html",context)


def contact(request):
    return render(request, "pages/contact.html")
