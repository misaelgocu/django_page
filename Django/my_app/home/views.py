from django.shortcuts import render

# Create your views here.
# Vista para la página de inicio
def index(request):
    return render(request, 'home/index.html')

# Vista para la página de contacto
def contact(request):
    return render(request, 'home/contacto.html')
 