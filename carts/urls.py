from . import views
from django.urls import path

urlpatterns = [
    path('', views.cart, name = 'carts'),
    path('add_cart/<int:product_id>/',views.add_cart, name = 'add_cart'),
    path('decrease_cart/<int:cart_item_id>/', views.decrease_cart, name='decrease_cart'),
    path('remove_cart/<int:product_id>/<int:cart_item_id>/', views.remove_cart, name='remove_cart'),
    path('checkout/', views.checkout, name = 'checkout'),

] 