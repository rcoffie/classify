from django.shortcuts import render
from item_engine.models import Category, Item
import datetime 
# import the logging library
import logging 
# Get an instance of a logger
logger = logging.getLogger('django')
# Create your views here.


def home(request):
    items = Item.objects.filter(is_sold=False)[0:3]
    categories = Category.objects.all()
    context = {
        'items':items, 
        'categories':categories,
        }
    logger.warning('Homepage was accessed at '+str(datetime.datetime.now())+' hours!\n')
    return render(request, "pages/home.html",context)


def contact(request):
    return render(request, "pages/contact.html")
