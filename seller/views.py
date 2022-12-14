from django.shortcuts import render,redirect
from common.models import Seller
from .models import Product
from django.http import JsonResponse

# Create your views here.
def home(request):
    Seller_data = Seller.objects.get(id = request.session['seller'])
    return render(request,'sellertemplates/home.html',{'data':Seller_data})



def product_cataloges(request):
    seller_products = Product.objects.filter(Seller = request.session['seller'])
    return render(request,'sellertemplates/product_cataloges.html',{'products':seller_products})




def add_product(request):
    if request.method == 'POST':
            product_name = request.POST['s_productname']
            product_description = request.POST['s_description']
            product_number = request.POST['s_productnumber']
            current_stock = request.POST['s_currentstock']
            product_image  = request.FILES['s_fileupload']
            price = request.POST['s_price']

            new_product = Product(product_name=product_name,product_description=product_description,product_number=product_number,current_stock=current_stock,product_image=product_image,price=price,Seller_id=request.session['seller'])
            new_product.save()
            msg = "product added successfully"
            


    return render(request,'sellertemplates/add_product.html')


def update_stock(request):
    update_stock = Product.objects.filter(Seller = request.session['seller'])
    if request.method == 'POST':
        new_stock =  request.POST['new_stock']
        product_id = request.POST['product_id']
        product = Product.objects.get(id = product_id)
        product.current_stock = product.current_stock + int (new_stock)
        product.save()
    return render(request,'sellertemplates/update_stock.html',{'stock':update_stock})


def change_password(request):
    msg = ''
    if request.method == 'POST':
      

        current_pass = request.POST['crnt_pswrd']
        new_pass = request.POST['new_pswrd']
        confirm_pass = request.POST['cnfrm_pswrd']

        seller_pass = Seller.objects.get(id = request.session['seller'])

        if seller_pass.seller_password == current_pass:
            if new_pass == confirm_pass:
                seller_pass.seller_password = new_pass
                seller_pass.save()
                msg = 'password changed successfully'
            else:
                msg = 'password does not match'
        else:
            msg = 'incorrect password'
            
    return render(request,'sellertemplates/change_password.html',{'msg':msg})


def recent_order(request):
    return render(request,'sellertemplates/recent_order.html')


def order_history(request):
    return render(request,'sellertemplates/order_history.html')


def profile(request):
    seller_profile = Seller.objects.get(id = request.session['seller'])
    return render(request,'sellertemplates/profile.html',{'sprofile':seller_profile})


def seller_signup(request):
    return render(request,'sellertemplates/seller_signup.html')



def logout(request):
    del request.session['seller']
    request.session.flush() # to remove session data from django session table
    return redirect('common:seller_login')


def get_stock(request):
    id = request.POST['id']
    product = Product.objects.get(id=id)
    product_name = product.product_name
    current_stock = product.current_stock
    p_id = product.id
    return JsonResponse({'p_name':product_name,'c_stock':current_stock,'pro_id':p_id})