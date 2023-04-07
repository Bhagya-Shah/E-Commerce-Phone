from django.shortcuts import render
from products.models import Product,SizeVariant,ColorVariant

from django.shortcuts import redirect,HttpResponseRedirect
# Create your views here.

def get_products(request,slug):

    try:
        product=Product.objects.get(slug=slug)
        context={'product':product}
        if request.GET.get('size'):
            size=request.GET.get('size')
            price=product.get_product_price_by_size(size)
            context['selected_size']=size
            context['updated_price']=price

        return render(request,'product/products.html',context=context)
    except Exception as e:
        # return render(request,'product/products.html')
        print(e)


