from django.shortcuts import render
from django.db.models import F

from store.models import Order, Product, OrderItem



def say_hello(request):
    # queryset = Product.objects.all()
    
    # Products: inventory = unit_price
    # queryset = Product.objects.filter(
    #     inventory=F('unit_price')
    # )
    # sorting
    product = Product.objects.order_by("unit_price")[0]
    # limiting results
    # queryset = Product.objects.all()[:5]
    # 
    queryset = OrderItem.objects.values('product_id')    
    context = {
        "queryset" : queryset
        # 'product': product,
    }
    return render(request, 'example.html', context)


