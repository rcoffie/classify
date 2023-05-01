from item_engine.models import Category, Item
from rest_framework import serializers




class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            "id",
            "name",
            "user",
            "created_on",
            "updated_on",
        ]
        read_only_fields = ["id","created_on","updated_on"]


class ItemSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Item
        fields = [
            "id",
            "name",
            "description",
            "price",
            "is_sold",
            "category",
            "item_image",
            "created_on",
            "updated_on",
        ]

        read_only_fields = ["id","created_on","updated_on",]

