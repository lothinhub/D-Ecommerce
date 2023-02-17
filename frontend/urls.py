from django.urls import path

from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('signin', views.signin, name="signin"),
    path('register', views.register, name="register"),
    path('cart', views.cart, name="cart"),
    path('product-detail', views.product_detail, name="product-detail"),
    path('store', views.store, name="store"),


]
