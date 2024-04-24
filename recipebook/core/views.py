from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login as auth_login
from .forms import customerRegistrationForm
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt

# Create your views here.
def login(request):
   
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            if user.is_superuser:
                return redirect('listing')  # Redirect superuser to attendance.html
            elif hasattr(user, 'customer'):  # Check if user is linked to an employee
                return redirect('recipelist')  # Redirect employee to markattendance.html
            else:
                return redirect('recipelist')  # Redirect for users who are neither
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'core/login.html')

def register(request):

    if request.method == 'POST':
        form = customerRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Assuming the form saves the user and creates an employee profile
            return redirect('login')  # Redirect to login page after successful registration
    else:
        form = customerRegistrationForm()
    return render(request, 'core/register.html',{'form':form})

def recipelist(request):
    return render(request, 'core/recipelist.html')

def recipeedit(request):
    return render(request, 'core/recipeedit.html')

def recipe(request):
    return render(request, 'core/recipe.html')

def listing(request):
    return render(request, 'core/listing.html')