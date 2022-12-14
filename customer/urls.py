from django.urls import path
from . import views

app_name = "customer"

urlpatterns = [
    path('home',views.home, name="home"),
    path('product_details/<int:pid>',views.product_details, name="product_details"),
    path('my_cart',views.my_cart),
    path('my_order',views.my_order),
    path('change_password',views.change_password , name='change_pass'),
    path('profile',views.profile),
    path('logout',views.logout),
    path('remove_item/<int:pid>',views.remove_item,name='remove_item'),
]