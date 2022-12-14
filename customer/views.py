from django.shortcuts import render,redirect
from seller.models import Product
from common.models import Customer
from customer.models import Cart


# Create your views here.
def home(request):
    product_list = Product.objects.all()
    return render(request,'customertemplates/home.html',{'products':product_list})

def product_details(request,pid):
    msg = ''
    product_details = Product.objects.get(id = pid)

    if request.method == "POST":
        product_exist = Cart.objects.filter(product_details = pid,customer = request.session['customer']).exists()
        if not product_exist:
            cart = Cart(customer_id = request.session['customer'], product_details_id = pid)
            cart.save()
        else:
            msg = "item already in cart"
    context ={
            'details':product_details,
            'msg': msg
    }
    return render(request,'customertemplates/product_details.html',context)
    # return render(request,'customertemplates/product_details.html',{'details':product_details})

def my_cart(request):
    cart = Cart.objects.filter(customer = request.session['customer'])
    return render(request,'customertemplates/my_cart.html',{'customer_cart' : cart})

def my_order(request):
    return render(request,'customertemplates/my_order.html')

def change_password(request):
    msg = ''
    if request.method == 'POST':
        customer = Customer.objects.get(id = request.session['customer'])

        current_pass = request.POST['crnt_pswrd']
        new_pass = request.POST['new_pswrd']
        confirm_pass = request.POST['cnfrm_pswrd']

        if customer.Customer_password == current_pass:
            if new_pass == confirm_pass:
                customer.Customer_password = new_pass
                customer.save()
                msg = 'password changed successfully'
            else:
                msg = 'password does not match'
        else:
            msg = 'incorrect password'
            
    return render(request,'customertemplates/change_password.html',{'msg':msg})



def profile(request):
    cust_prof = Customer.objects.get(id = request.session['customer'])
    return render(request,'customertemplates/profile.html',{'profile':cust_prof})



def logout(request):
    return render(request,'customertemplates/logout.html')



def remove_item(request,pid):
    cart_item = Cart.objects.get(product = pid,Customer = request.session['customer'])
    cart_item.delete()
    return redirect('customer:my_cart')



def logout(request):
    del request.session['customer']
    request.session.flush() # to remove session data from django session table
    return redirect('common:customer_login')


