from django_filters import FilterSet, DateTimeFilter
from .models import Product, News
from django.forms import DateTimeInput

class ProductFilter(FilterSet):
   class Meta:

       model = Product

       fields = {
           'name': ['icontains'],
           # количество товаров должно быть больше или равно
           'quantity': ['gt'],
           'price': [
               'lt',  # цена должна быть меньше или равна указанной
               'gt',  # цена должна быть больше или равна указанной
           ],
       }

class NewsFilter(FilterSet):
    added_after = DateTimeFilter(
        field_name='added_at',
        lookup_expr='gt',
        widget=DateTimeInput(
            format='%Y-%m-%dT%H:%M',
            attrs={'type': 'datetime-local'},
        ),
    )

    class Meta:
        model = News
        fields = {
            'title',
            'category',
        }