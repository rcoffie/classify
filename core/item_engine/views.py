from django.shortcuts import render, get_object_or_404, redirect
from . models import Category, Item
from .forms import ItemForm
# Create your views here.


def item_detail(request, id):
    item = get_object_or_404(Item, id=id)
    related_items = Item.objects.filter(category=item.category,).exclude(id=id)[0:3]
    context = {'item':item, 'related_items':related_items,}
    return render(request, 'item_engine/item-detail.html',context)


def add_item(request):
    form = ItemForm()
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()
            return redirect('item_detail', id=item.id)
        else:
            form = ItemForm()
    context = {'form':form}
    return render(request, 'item_engine/add-item-form.html',context)