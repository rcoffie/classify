from item_engine.models import Item
from rest_framework import serializers


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = [
            "id",
            "name",
            "description",
            "price",
            "price",
            "is_sold",
            "category",
            "item_image",
            "created_on",
            "updated_on",
        ]
        read_only_fields = ["id","created_on","updated_on",]
