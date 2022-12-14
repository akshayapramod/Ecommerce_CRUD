from django.shortcuts import render,redirect
from .models import Customer,Seller
import random
from django.core.mail import send_mail
from django.conf import settings
from django.http import JsonResponse
# Create your views here.
def home(request):
    return render(request,'commontemplates/home.html')

def customer_reg(request):

    if request.method == 'POST':


        cst_name = request.POST['c_name'] # when submit button clicked
        cst_mobile = request.POST['c_mobile'] # here we get data input in tetbox, 
        cst_address = request.POST['c_address']
        cst_gender = request.POST['c_gender']
        cst_mail = request.POST['c_mail']
        cst_pass = request.POST['c_pass']
        cst_pic = request.FILES['c_pic']
        
        new_customer = Customer(
            customer_name = cst_name, customer_number = cst_mobile, 
            customer_address = cst_address, customer_gender = cst_gender, 
            customer_email = cst_mail,customer_password=cst_pass,
            customer_image = cst_pic)
        new_customer.save()

    return render(request,'commontemplates/customer_reg.html')

def seller_reg(request):
    if request.method == 'POST':
        seller_name = request.POST['seller_name']
        seller_email = request.POST['seller_email']
        seller_phone = request.POST['seller_phone']
        seller_address = request.POST['seller_address']
        company_name = request.POST['company_name']
        seller_acc_holdername = request.POST['acc_hold_name']
        seller_ifsc = request.POST['ifsc']
        seller_branch = request.POST['branch']

        seller_acc_number = request.POST['acc_number']

        seller_image = request.FILES['seller_image']
        seller_username = random.randint(1111,9999)
        seller_password = 'sel-'+ seller_name.lower() + str(seller_username)
        message = 'hai! your username is ' + str(seller_username) + 'and temporary password is ' + seller_password

        new_Seller = Seller(seller_name = seller_name,

        seller_email = seller_email,
        seller_phone=seller_phone,

        seller_address=seller_address,
        company_name=company_name,
        acc_holder=seller_acc_holdername,
        ifsc=seller_ifsc,
        branch=seller_branch,
        acc_number = seller_acc_number,
        seller_username=seller_username,seller_password=seller_password,
        seller_pic=seller_image)

        send_mail(
            'username and temporary password',
            message,
            settings.EMAIL_HOST_USER,
            [seller_email,],
            fail_silently=False
        )
        new_Seller.save()

    return render(request,'commontemplates/seller_reg.html')

def customer_login(request): 
    msg = ""                                                               
    if request.method == 'POST':
        c_email = request.POST['customer_email']
        c_password = request.POST['customer_password']

        try:
            customer = Customer.objects.get(customer_email = c_email, customer_password = c_password )
            request.session['customer'] = customer.id
            return redirect('customer:home')
        except:
            msg = 'incorrect username or password '

    return render(request,'commontemplates/customer_login.html',{'msg':msg}) 

    # return render(request,'commontemplates/customer_login.html')                     

def seller_login(request):
    msg =''
    if request.method == 'POST':
        seller_username = request.POST['username']
        seller_password = request.POST['password']
        try:
            user = Seller.objects.get(seller_username = seller_username,seller_password = seller_password )
            # if username and password is correct, we set a session variable with key 'seller'
            # session variable can be accessed throughout the application 

            # working of django session 
            # when username and password is correct, we set a session variable with key( here key  'seller') and 
            # unique value for each seller (here value is the primary key of the logged in seller )
            # if a seller with primarykey to logs in session key will be 'seller' and value will be 2

            # when we set a session ,key and value will be stored in django_session table inside database in encrypted format

            # encrypted key will be send with http response to the client (browser)

            # in the client side (browser),the key received from the server will be stored in browser storage(cookies)

            # when the user request any page (eg: cart page) from the same browser, the same key stored inside cookies
            # sending to the server through http request

            # when the request reaches the server, it will look for the key stored in cookie  to match with 
            # django_session table inside the database to find the corresponding user 


            request.session['seller'] = user.id
            return redirect('seller:seller_home')
        except:
            msg = 'username or password incorrect'

    return render(request,'commontemplates/seller_login.html',{'msg':msg})

def email_exist(request):

    e_mail = request.POST['email']       #here email is the kay inside jason

    status = Customer.objects.filter(customer_email = e_mail).exists()

    return JsonResponse({'status':status})
