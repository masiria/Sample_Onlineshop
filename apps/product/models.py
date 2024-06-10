from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    parent = models.ForeignKey(
        'Category', on_delete=models.PROTECT, blank=True, null=True, related_name='sub_categories'
    )

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    description = models.TextField(blank=True, null=True)
    price = models.IntegerField(default=0)
    discount = models.SmallIntegerField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    quantity = models.IntegerField(default=0)
    thumbnail = models.ImageField(upload_to='products/%Y/%m/%d')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='products')
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='products')

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='images')

    def __str__(self):
        return self.product


class ProductAttribute(models.Model):
    name = models.CharField(max_length=100)
    value = models.CharField(max_length=255)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='attributes')

    def __str__(self):
        return self.name


class Review(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    rating = models.SmallIntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey(
        'self', on_delete=models.PROTECT, null=True, blank=True, related_name='replies'
    )
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='comments')

    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=75)
    slug = models.SlugField(max_length=75, unique=True, blank=True)
    product = models.ManyToManyField(Product, related_name='tags')

    def __str__(self):
        return self.name
