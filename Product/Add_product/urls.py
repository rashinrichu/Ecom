from django.urls import path,include
from Add_product import views

urlpatterns = [
    path('',views.home,name='home'),
    path("CategoryPage",views.CategoryPage,name="CategoryPage"),
    path("Product",views.Product,name="Product"),
    path("AddCategory",views.AddCategory,name="AddCategory"),
    path("AddProduct",views.AddProduct,name="AddProduct"),
    path("ProductDetails",views.ProductDetails,name="ProductDetails"),
    path('Tables',views.Tables,name='Tables')

]