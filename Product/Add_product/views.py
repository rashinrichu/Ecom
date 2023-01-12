from django.shortcuts import render,redirect
from . models import *
# Create your views here.
def home(request):
    return render(request,'home.html')
def Product(request):
    category=CategoryModel.objects.all()
    context={'Category':category}
    return render(request,'adddproduct.html',context)


def AddCategory(request):
    if request.method == 'POST':
        categoryname=request.POST['Name']
        data = CategoryModel(Name=categoryname)
        data.save()
        print('added')
        # messages.info(request, 'New User Added')
        return redirect('home')


def CategoryPage(request):
      return render(request,'addcategory.html')


def AddProduct(request):
    if request.method=='POST':
        pprice=request.POST['Price']
        pdes=request.POST['Description']
        pqty=request.POST['Quantity']
        select=request.POST['select']
        category=CategoryModel.objects.get(id=select)
        data = ProductModel(Price=pprice,Description=pdes,Quantity=pqty,Category=category)
        
        data.save()
        print('added')
        return redirect('home')


def ProductDetails(request):
    Product_detail = ProductModel.objects.all()
    return render(request,'productdetail.html',{'product':Product_detail})


def Tables(request):
        category=CategoryModel.objects.all()
        Product=ProductModel.objects.all()
        return render(request,'table.html',{'cdata':category,'pdata':Product})
    
