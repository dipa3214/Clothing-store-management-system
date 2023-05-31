from django.shortcuts import render
from django.views import View
from .models import Product,Cart,OrderPlaced,Customer

#def home(request):
 #return render(request, 'app/home.html')
class Product_View(View):
  def Get(self,request):
      topwears = Product.object.filter(category='TW')
      babydress=Product.object.filter(category='BD')
      watch=Product.object.filter(category='W')
      return render(request,'app/home.html', {'topwears':topwears,'babydress':babydress,'watch': watch})

 

def product_detail(request):
 return render(request, 'app/productdetail.html')

def add_to_cart(request):
 return render(request, 'app/addtocart.html')

def buy_now(request):
 return render(request, 'app/buynow.html')

def profile(request):
 return render(request, 'app/profile.html')

def address(request):
 return render(request, 'app/address.html')

def orders(request):
 return render(request, 'app/orders.html')

def change_password(request):
 return render(request, 'app/changepassword.html')

def mobile(request):
 return render(request, 'app/mobile.html')

def login(request):
 return render(request, 'app/login.html')

def customerregistration(request):
 return render(request, 'app/customerregistration.html')

def checkout(request):
 return render(request, 'app/checkout.html')
