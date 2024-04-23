from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, 'core/login.html')

def register(request):
    return render(request, 'core/register.html')

def recipelist(request):
    return render(request, 'core/recipelist.html')

def recipeedit(request):
    return render(request, 'core/recipeedit.html')

def recipe(request):
    return render(request, 'core/recipe.html')

def listing(request):
    return render(request, 'core/listing.html')