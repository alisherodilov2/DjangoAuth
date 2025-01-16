from django.shortcuts import render ,redirect
from .forms import UserCreationForm , LoginForm
from django.contrib.auth import authenticate, login, logout


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
                return render(request, 'webapp/index.html')

            return render(request, 'webapp/index.html')
    context = {'form': form}
    return render(request, 'webapp/login.html', context=context)



def logout_view(request):
    logout(request)
    return redirect('home')

