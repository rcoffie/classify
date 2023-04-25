from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.urls import reverse
from item_engine.forms import ItemForm
from item_engine.models import Category, Item




class TestItemView(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="password")
        self.client.login(username="testuser", password="password")
        self.category = Category.objects.create(name="category name", user=self.user)
        self.item = Item.objects.create(
            name="name",
            description="description",
            price=78.0,
            category=self.category,
            item_image="lg.jpg",
            created_by=self.user
        )
        self.data = {
            "name":"name",
            "description":"description",
            "price":78.9,
            "category":"category",
            "item_image":"img.jpg",
            
        }
        self.add_item = Item(
            name='name', 
            category=self.category,
            item_image='ll.jpg',
            price= 78.9, 
            created_by=self.user,
        )

    def test_item_list_view(self):
        url = reverse("item_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "item_engine/item-list.html")

    def test_item_detail_view(self):
        url = reverse("item_detail", args=[str(self.item.id)])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed("item_engine/item-detail.html")


    def test_add_item_view(self):
        url = reverse('add_item')
        response = self.client.get('/item_engine/add_item/')
        self.assertEqual(response.status_code, 200)
        response = self.client.post(url, data=self.data)


    def test_update_item_view(self):
        response = self.client.post(reverse('edit_item', args=[self.item.id]),{
            'name':'update name',
            'description':'This is an update description'
        })

        self.assertEqual(response.status_code,200)


    def test_delete_post(self):
        self.client.login(username="testuser", password="testpassword")
        response = self.client.post(reverse('delete_item', args=[self.item.id]))
        self.assertEqual(response.status_code, 302)
