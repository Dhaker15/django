from django.shortcuts import render
from .models.phone import Product,Category
from .models.news import News
from math import ceil

def index(request):
    news = News.objects.all()

    params = {'news':news}
    return render(request, 'home.html',params)



def tv(request):
    return render(request,'tv.html')



def phone(request):
    products = None
    categories = Category.get_all_categories()
    categoryID = request.GET.get('category')
    if categoryID:
        products = Product.get_all_products_by_categoryid(categoryID)
    else:
        products = Product.get_all_products();

    data ={'data':products,'data1':categories}
    return render(request, 'phone.html',data)


def laptop(request):
    return render(request,'laptop.html')



def productView(request, myid):
    product = Product.objects.filter(id=myid)
    print(product)


    return render(request, 'productview.html', {'product':product[0]})