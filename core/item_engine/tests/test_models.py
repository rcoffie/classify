from django.test import TestCase
from item_engine.models import Category, Item
from django.contrib.auth.models import User

# Create your tests here.

class TestCategoryModels(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        


    def test_create_category(self):
        category = Category.objects.create(user=self.user,name='cat1')
        self.assertEqual(Category.objects.count(),1)
        self.assertEqual(str(category), "cat1")


class TestItemModels(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpassword")
        
    
    def test_create_item(self):
        category = Category.objects.create(user=self.user,name="cat")
        self.assertEqual(Category.objects.count(),1)
        item = Item.objects.create(name="name",description="description",price=56.0, category=category,created_by=self.user)
        self.assertEqual(Item.objects.count(), 1)
        self.assertEqual(str(item), 'name')
        
        
        
        
