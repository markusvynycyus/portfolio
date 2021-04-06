from django.shortcuts import render
from .models import Contact

# Create your views here.


# Home/Index View
def index(request):
    return render(request, 'portfolio/home.html')

#Portfolio View
def portfolio(request):
    return render(request, 'portfolio/portfolio.html')

# About View
def sobre(request):
    return render(request, 'portfolio/sobre.html')

# Contact View
def contact(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        form = Contact(nome=nome, email=email, subject=subject, message=message)
        # Saving Form data to Database
        form.save()

        return render(request, 'portfolio/contact.html')
    else:
        return render(request, 'portfolio/contact.html')


