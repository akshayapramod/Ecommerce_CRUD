from django.urls import path
from . import views
app_name = 'seller'
urlpatterns = [
    path('seller_home',views.home,name='seller_home'),
    path('product_cataloges',views.product_cataloges),
    path('add_product',views.add_product),
    path('update_stock',views.update_stock, name='update_stock'),
    path('change_password',views.change_password,name='change_pass'),
    path('recent_order',views.recent_order),
    path('order_history',views.order_history),
    path('profile',views.profile),
    path('seller_signup',views.seller_signup),
    path('get_stock',views.get_stock,name='get_stock'),
]