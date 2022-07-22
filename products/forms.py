from .models import Product
from django import forms
class CreateNewProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = (
            "name",
            "description",
            "image",
            "image_alt_text",
            "inventory",
            "category",
            "colour",
            "keywords",
            "sku",
            "is_washable",
            "wash_instructions",
            "care_instructions",
            "weight",
            "size",
            "unit_cost_price",
            "retail_price",
            "sale_price",
            "in_stock",
            "is_active",
        )
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "sku": forms.NumberInput(attrs={"class": "form-control"}),
            "category": forms.Select(attrs={"class": "form-control"}),
            "colour": forms.Select(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control"}),
            "keywords": forms.TextInput(attrs={"class": "form-control"}),
            "is_washable": forms.CheckboxInput(),
            "image": forms.FileInput(attrs={"class": "form-control"}),
            "image_alt_text": forms.TextInput(attrs={"class": "form-control"}),
            "wash_instructions": forms.Textarea(attrs={"class": "form-control"}),
            "care_instructions": forms.Textarea(attrs={"class": "form-control"}),
            "weight": forms.NumberInput(attrs={"class": "form-control"}),
            "size": forms.TextInput(attrs={"class": "form-control"}),
            "unit_cost_price": forms.NumberInput(attrs={"class": "form-control"}),
            "retail_price": forms.NumberInput(attrs={"class": "form-control"}),
            "sale_price": forms.NumberInput(attrs={"class": "form-control"}),
            "inventory": forms.NumberInput(attrs={"class": "form-control"}),
            "in_stock": forms.CheckboxInput(),
            "is_active": forms.CheckboxInput()
        }
