from django.shortcuts import render
from common.models import Customer,Seller
# Create your views here.
def home(request):
    return render(request,'admintemplates/home.html')

def approve_seller(request):
    seller = Seller.objects.all()
    return render(request,'admintemplates/approve_seller.html',{"seller_list":seller})


def view_seller(request):
    return render(request,'admintemplates/view_seller.html')


def view_customer(request):
    return render(request,'admintemplates/view_customer.html')

    
def approve_customer(request):
    Customers = Customer.objects.all()
    return render(request,'admintemplates/approve_customer.html',{"customer_list":Customers})