from django.urls import path
from . import views
from .controllers import products_controller
urlpatterns = [
    path('', views.home, name='home'),
    path('my-login', views.my_login, name='my-login'),
    path('logout', views.logout_view, name='logout'),
    path('dashboard', products_controller.ProductsController.index, name='dashboard'),
    path('register', views.register, name='register'),
    path('products', products_controller.ProductsController.get_all, name='get-all-products'),
    path('products/create', products_controller.ProductsController.create, name='create-product'),
]



