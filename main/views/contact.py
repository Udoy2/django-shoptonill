from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from ..models import Contact


class ContactView(View):
    def get(self, request):
        return render(request, 'pages/contact.html')

    def post(self, request):
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        if (Contact.saveContact(name, email, message)):
            return redirect('home')

        return redirect('contact')
