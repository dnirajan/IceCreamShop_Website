from django.http import HttpResponse
from django.shortcuts import render
from home.models import Contact
from datetime import datetime
from django.contrib import messages


# username: Nirajan pw: nirajandada
# Create your views here.
def index(request):
    # return HttpResponse("This is homepage")
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def services(request):
    return render(request, 'services.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        queries = request.POST.get('queries')
        contact = Contact(name=name, email=email, phone=phone, address=address, queries=queries, date=datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent!')

    return render(request, 'contact.html')
