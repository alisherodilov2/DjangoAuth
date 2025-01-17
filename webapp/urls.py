from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('my-login', views.my_login, name='my-login'),
    path('logout', views.logout_view, name='logout'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('register', views.register, name='register'),
    # create new product
    path('create-product', views.create_product, name='create-product'),
]




