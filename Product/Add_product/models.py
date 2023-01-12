from django.db import models

# Create your models here.
class CategoryModel(models.Model):
    Name=models.CharField(max_length=120)
    
    
    
class ProductModel(models.Model):
    Category=models.ForeignKey(CategoryModel,on_delete=models.CASCADE,null=True)
    Price=models.IntegerField()
    Description=models.TextField()
    Quantity=models.IntegerField()