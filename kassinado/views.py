from django.shortcuts import render
from .models import Product , Comments

# Create your views here.
def index(request):
    return render(request,"home.html",{
        "products" : Product.objects.all()
    })
def product(request,id):
    
    if request.method == "POST":
        comment = request.POST.get("the_comment")
        Comments.objects.create(text=comment,product=Product.objects.get(pk=id))
    product = Product.objects.get(pk=id)

    Product.objects.filter(pk=id).update(views = product.views+1 )
    
    return render(request,"product.html",{
        "product" : Product.objects.get(pk=id),
        "comments" : Comments.objects.filter(product=Product.objects.get(pk=id))
        })
