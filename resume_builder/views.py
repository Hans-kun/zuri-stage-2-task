from django.shortcuts import render,HttpResponse
from .models  import Customer, Skills, Technical, Experience, Education
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def index(request):
    customer = Customer.objects.all()
    skills = Skills.objects.all()
    technical = Technical.objects.all()
    experience = Experience.objects.all()
    education = Education.objects.all()

    subject = 'Thank you for contacting me'
    if request.method == 'POST':
        name = request.POST.get('sender_name')
        email = request.POST.get('sender_email')
        body = request.POST.get('body')
        message = f'{name}, {email} {body}'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['okpalahans@gmail.com',]
        send_mail( subject, message, email_from, recipient_list )
        return HttpResponse("Thank you for contacting me I'll get back to you soon ")
    context = {'customer': customer, 'skills': skills, 'technical': technical, 'experience': experience, 'education': education}
    return render(request, 'index.html', context)


# def email(request):
