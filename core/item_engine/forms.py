from django.forms import ModelForm

from .models import Item


class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = [
            "name",
            "description",
            "price",
            "category",
            "item_image",
        ]


class EditItemForm(ModelForm):
    class Meta:
        model = Item
        fields = [
            "name",
            "description",
            "price",
            "category",
            "item_image",
            "is_sold",
        ]

    # def __init__(self, *args, **kwargs):
    #     super(ItemForm, self).__init__(*args, **kwargs)

    #     for name, field in self.fields.items():
    #         field.widget.attrs.update({'class':'form-control'})
