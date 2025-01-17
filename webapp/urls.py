from django.urls import path
from . import views
from .controllers import products_controller
urlpatterns = [
    path('', views.home, name='home'),
    path('my-login', views.my_login, name='my-login'),
    path('logout', views.logout_view, name='logout'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('register', views.register, name='register'),
    # create new product
    path('create-product', views.create_product, name='create-product'),
    # path('get-all-products', views.get_all_products, name='get-all-products'),
    path('products', products_controller.ProductsController.get_all, name='get-all-products'),
    path('products/create', products_controller.ProductsController.create, name='create-product'),
    path('products/dashboard', products_controller.ProductsController.index, name='dashboard'),
]




