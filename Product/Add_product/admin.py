from django.contrib import admin
from Add_product.models import CategoryModel,ProductModel

# Register your models here.
@admin.register(CategoryModel)
class CategoryDetailAdmin(admin.ModelAdmin):
    list_display=['id','Name']
    list_editable=['Name']    
    
   
    
    
@admin.register(ProductModel)
class ProductDetailAdmin(admin.ModelAdmin):
    list_display=['id','Price','Description','Quantity','Category']
    list_display_links=['Category']
    list_editable=['id','Price','Description','Quantity']
    

    
    
    
