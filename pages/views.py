from email import message
import email
from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import send_mail
from pages.forms import ContactForm

# Create your views here.
def index(request):
    contact_form = ContactForm()
    if request.method == 'POST':
        contact_form = ContactForm(data = request.POST)

        if contact_form.is_valid():
            name = request.POST.get('name', '')
            subject = 'Mensaje del website MA-graphicstudio'
            message = request.POST.get('message', '')
            from_email = request.POST.get('email', '')
            if subject and message and from_email:
                try:
                    send_mail(
                    subject,
                    "{}<{}> Escribió el siguiente mensaje:\n\n{}".format(name,from_email,message),
                    from_email,
                    ['magraphicstudio.contact@gmail.com'],
                    )
                    return redirect(reverse('index')+"?ok#contact")
                except:
                    return redirect(reverse('index')+"?fail#contact")

    return render(request,'pages/index.html',{'contact_form':contact_form})

def error_404_view(request, exception):
    return render(request,'pages/404.html')