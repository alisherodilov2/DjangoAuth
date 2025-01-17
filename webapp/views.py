from django.shortcuts import render ,redirect

from .models import Products
from .forms import ProductForm, UserCreationForm , LoginForm
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required
def home(request):
    return render(request, 'webapp/index.html')




def my_login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return render(request, 'webapp/dashboard.html')

            return render(request, 'webapp/index.html')
    context = {'form': form}
    return render(request, 'webapp/login.html', context=context)



def logout_view(request):
    logout(request)
    return redirect('home')





def register(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('my-login')
    
    context = {'form': form}
    return render(request, 'webapp/register.html', context=context)




@login_required(login_url='my-login')
def dashboard(request):    
    context = {
        'user': request.user,
        'products': Products.objects.all()
    }
    return render(request, 'webapp/dashboard.html', context=context)


@login_required(login_url='my-login')
def create_product(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    context = {'form': form}
    return render(request, 'webapp/create-product.html', context=context)

    
