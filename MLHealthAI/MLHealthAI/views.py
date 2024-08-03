from django.http import HttpResponse
from django.shortcuts import render
from .models import Contact_page_model, Newseletter_page

def mainpage(request):
    return render(request, "English/index.html")
    
def about_page(request):
    return render(request, "English/about.html")

def blog_single_page(request):
    return render(request, "English/blog-single.html")

def blog_page(request):
    return render(request, "English/blog.html")

def contact_page(request):
    return render(request, "English/contact.html")

def portfolio_page(request):
    return render(request, "English/portfolio.html")

def services_page(request):
    return render(request, "English/services.html")

def error_404_handler(request, exception):
    return render(request, "Error/page404.html")

def create_contact(request):
    if request.method =='POST':
        nameform = request.POST.get('nameform',False)
        email=request.POST.get('email',False)
        subject=request.POST.get('subject', False)
        message=request.POST.get('message', False)

        new_create_contact=Contact_page_model(nameform=nameform,email=email,subject=subject,message=message,)
        
        new_create_contact.save()
        return HttpResponse('Contact saved successfully.')
    return HttpResponse('Invalid request method.', status=405)

def create_newsletter(request):
    if request.method =='POST':
       
        Email=request.POST.get('Email',False)
        new_create_newsletter=Newseletter_page(Email=Email,)
        
        new_create_newsletter.save()
        return HttpResponse('Contact saved successfully.')
    return HttpResponse('Invalid request method.', status=405)