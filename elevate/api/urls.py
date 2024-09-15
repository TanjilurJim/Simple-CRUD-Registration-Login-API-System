from django.urls import path

from . import views

from rest_framework.urlpatterns import format_suffix_patterns

from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [

    path('products', views.product_list, name='products'),
    path('product/<int:pk>',views.product, name='product'),
    path('register',views.register, name='register'),
    path('login',obtain_auth_token, name='login'),
    path('',views.home, name='home'),
    path('products_list',views.products, name='products_list'),








]


urlpatterns = format_suffix_patterns(urlpatterns) #allows json in our browser

 