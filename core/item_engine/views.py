from django.contrib import messages
from django.contrib.auth.decorators import login_required
# from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from .forms import EditItemForm, ItemForm
from .models import Category, Item

# Create your views here.


def item_list(request):
    query = request.GET.get("query", "")
    category_id = request.GET.get("category", 0)
    categories = Category.objects.all()
    items = Item.objects.filter(is_sold=False)
    if category_id:
        items = Item.objects.filter(category_id=category_id)
    if query:
        items = items.filter(Q(name__icontains=query) | Q(description__icontains=query))
    context = {
        "items": items,
        "query": query,
        "categories": categories,
        "category_id": int(category_id),
    }
    return render(request, "item_engine/item-list.html", context)


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


@login_required(login_url="signup")
def add_item(request):
    form = ItemForm()
    if request.method == "POST":
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()
            messages.success(request, "Added successfully")
            return redirect("item_detail", id=item.id)
        else:
            form = ItemForm()
    context = {"form": form}
    return render(request, "item_engine/add-item-form.html", context)


@login_required(login_url="signup")
def edit_item(request, id=id):
    form = EditItemForm()
    item = get_object_or_404(Item, id=id)
    if request.method == "POST":
        form = EditItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            item = form.save(commit=False)
            item.save()
            messages.info(request, "Updated successfully")
            return redirect("item_detail", id=item.id)
    else:
        form = EditItemForm(instance=item)
    context = {"form": form}
    return render(request, "item_engine/edit-item-form.html", context)


@login_required(login_url="signup")
def delete_item(request, id):
    item = get_object_or_404(Item, id=id)
    item.delete()
    messages.info(request, "item deleted successfully")
    return redirect("dashboard")
