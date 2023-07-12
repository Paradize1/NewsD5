from django import forms
from django.core.exceptions import ValidationError

from .models import Product, News


class ProductForm(forms.ModelForm):
    description = forms.CharField(min_length=20)
    class Meta:
        model = Product
        fields = ['name','description','category','price','quantity',]
    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get("name")
        description = cleaned_data.get("description")

        if name == description:
            raise ValidationError("Описание не должно быть идентично названию.")
        return cleaned_data

    def clean_name(self):
        name = self.cleaned_data["name"]
        if name[0].islower():
            raise ValidationError("Название должно начинаться с заглавной буквы")
        return name

class NewsForm(forms.ModelForm):
    text = forms.CharField(min_length=20)

    class Meta:
        model = News
        fields = ['title', 'text', 'category',]

    def clean(self):
        cleaned_data = super().clean()
        text = cleaned_data.get("text")
        title = cleaned_data.get("title")

        if title == text:
            raise ValidationError(
                "Описание не должно быть идентично названию."
            )

        return cleaned_data