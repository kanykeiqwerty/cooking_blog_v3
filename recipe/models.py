from django.db import models
from category.models import Category
# Create your models here.






class Product(models.Model):
    title=models.CharField(max_length=100)
    ingredients=models.TextField()
    recipe=models.TextField()
    
    category=models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    image=models.ImageField(upload_to='images', null=True, blank=True)



    class Meta:
        ordering=['title']

    def __str__(self) -> str:
        return self.title