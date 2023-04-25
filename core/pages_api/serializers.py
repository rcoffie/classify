from rest_framework import serializers 
from item_engine.models import Item


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item 
        fields = ['id','name','description','price','is_sold','category','item_image']
 