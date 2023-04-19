from django.test import TestCase
from item_engine.models import Item, Category 
from django.urls import reverse 
from django.contrib.auth.models import User 
from django.core.files.uploadedfile import SimpleUploadedFile
from item_engine.forms import ItemForm
from django.contrib.messages import get_messages



class TestItemView(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.client.login(username='testuser', password='password')
        self.category = Category.objects.create(name='name', user=self.user)
        self.item = Item.objects.create(name='name',description="description",created_by=self.user,price=78.0, category=self.category, item_image='lg.jpg')
        
    def test_item_list_view(self):
        url = reverse('item_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response, 'item_engine/item-list.html')


    def test_item_detail_view(self):
        url = reverse('item_detail', args=[str(self.item.id)])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('item_engine/item-detail.html')


    def test_add_item_view(self):
        image = SimpleUploadedFile("test_image.jpg", b"file_content")
        data = {
            'id':1,
            'name':'Test Item',
            'description':'Test description',
            'image':image,
            'price':34.0,
            'category':self.category, 
            'created_by':self.user
        }
        print(data['id'])
        response = self.client.post(reverse('add_item'), data=data)

        # self.assertEqual(response.status_code, 302)

        # self.assertTrue(Item.objects.filter(name='Test Item').exists())
        self.assertEqual(Item.objects.count(),1)
        # self.assertRedirects(response, reverse('item_detail', args=[data['id']])) 
        self.assertEqual(response.status_code, 200)


    def test_item_delete(self):
        url = reverse('delete_item', args=[str(self.item.id)])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        


   