from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from .forms import EditItemForm, ItemForm
from .models import Category, Item
from django.contrib.auth.decorators import login_required
# Create your views here.


def item_detail(request, id):
    item = get_object_or_404(Item, id=id)
    related_items = Item.objects.filter(
        category=item.category,
    ).exclude(
        id=id
    )[0:3]
    context = {
        "item": item,
        "related_items": related_items,
    }
    return render(request, "item_engine/item-detail.html", context)

@login_required(login_url='signup')
def add_item(request):
    form = ItemForm()
    if request.method == "POST":
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()
            messages.success(request,'Added successfully')
            return redirect("item_detail", id=item.id)
        else:
            form = ItemForm()
    context = {"form": form}
    return render(request, "item_engine/add-item-form.html", context)

@login_required(login_url='signup')
def edit_item(request, id=id):
    form = EditItemForm()
    item = get_object_or_404(Item, id=id)
    if request.method == "POST":
        form = EditItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            item = form.save(commit=False)
            item.save()
            messages.info(request,'Updated successfully')
            return redirect("item_detail",id=item.id)
    else:
        form = EditItemForm(instance=item)
    context = {"form": form}
    return render(request, "item_engine/edit-item-form.html", context)

@login_required(login_url='signup')
def delete_item(request, id):
    item = get_object_or_404(Item, id=id)
    item.delete()
    messages.info(request,"item deleted successfully")
    return redirect("dashboard")
    
