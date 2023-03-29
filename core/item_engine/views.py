from django.shortcuts import render, get_object_or_404
from . models import Category, Item
# Create your views here.


def item_detail(request, id):
    item = get_object_or_404(Item, id=id)
    related_items = Item.objects.filter(category=item.category,)
    context = {'item':item, 'related_items':related_items,}
    return render(request, 'item_engine/item-detail.html',context)