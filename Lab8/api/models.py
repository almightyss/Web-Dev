from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True, default='none')
    
    def __str__(self):
        return f"{self.id}: {self.name}"

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField(default=1)
    description = models.TextField(default='buy new')
    count = models.IntegerField(default=1)
    is_active = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id}: {self.name}, price:{self.price}, cnt:{self.count}, is_active:{self.is_active}, category:{self.category.name}"
