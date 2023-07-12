from django.db import models
from django.core.validators import MinValueValidator
from django.urls import reverse

# Товар для нашей витрины
class Product(models.Model):
    name = models.CharField(max_length=50,unique=True,)
    description = models.TextField()
    quantity = models.IntegerField(validators=[MinValueValidator(0)],)
    category = models.ForeignKey(
        to='Category',
        on_delete=models.CASCADE,
        related_name='products',)
    price = models.FloatField(
        validators=[MinValueValidator(0.0)],)

    def __str__(self):
        return f'{self.name.title()}: {self.description[:10]}'

    def get_absolute_url(self):
        return reverse('product_detail', args=[str(self.id)])


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name.title()


class News(models.Model):
    title = models.CharField(max_length=50, unique=True, )
    text = models.TextField()
    category = models.ForeignKey(
        to='Category',
        on_delete=models.CASCADE,
        related_name='news',)
    added_at = models.DateTimeField(auto_now=True,)

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return reverse('news_detail', args=[str(self.id)])