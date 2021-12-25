from django.shortcuts import render
from .models import Product


def PostProduct(request):
    if request.method == 'POST':
        data = request.POST
        name = data['name']
        weight = data['weight']
        price = data['price']
        product = Product(name=name, weight=weight, price=price)
        product.save(using='products_db')
        return render(request, 'product.html', {'msg': 'Product Created Successfully!!'})
    return render(request, 'product.html')
