from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'users/index.html')

def bicicletas(request):
    return render(request,'users/bicicletas.html')

def iniciosesion(request):
    return render(request,'users/iniciosesion.html')

def registro(request):
    return render(request,'users/registro.html')