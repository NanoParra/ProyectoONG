from django.shortcuts import render

# Create your views here.
def index(request):
    contexto={'mensaje': 'Hola mundo'}
    return render(request, 'main.html');
   
