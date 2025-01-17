from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from ..models import Products
from ..forms import ProductForm

class ProductsController:
    @staticmethod
    @login_required(login_url='my-login')
    def index(request):
        context = {
            'user': request.user,
            'products': Products.objects.all()
        }
        return render(request, 'webapp/dashboard.html', context=context)

    @staticmethod
    @login_required(login_url='my-login') 
    def create(request):
        form = ProductForm()
        if request.method == 'POST':
            form = ProductForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('dashboard')
        context = {'form': form}
        return render(request, 'webapp/create-product.html', context=context)

    @staticmethod
    def get_all(request):
        products = Products.objects.all()
        products_list = []
        
        for product in products:
            products_list.append({
                'id': product.id,
                'name': product.name,
                'price': str(product.price),
                'description': product.description
            })
            
        return JsonResponse({'products': products_list})
