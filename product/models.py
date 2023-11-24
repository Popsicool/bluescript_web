from django.db import models
from django.contrib.auth.models import User

# Create your models here
# 
SIZE_CHOICE = (
    ('S', 'small'),
    ('M', 'medium'),
    ('L', 'large'),
    ('XL', 'extra large'),
    ('XXL', 'plus size')
)


class Category(models.Model):
    name = models.CharField(max_length=250)
    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=250)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.PositiveIntegerField(default=0)
    quantity = models.PositiveIntegerField(default=1)
    color = models.CharField(max_length=50)
    description = models.TextField()
    size = models.CharField(choices=SIZE_CHOICE, default=SIZE_CHOICE[1][0], max_length=3)
    image = models.ImageField(upload_to='product/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product')