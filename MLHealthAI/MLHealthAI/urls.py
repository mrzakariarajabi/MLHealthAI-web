"""
URL configuration for MLHealthAI project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
##
from django.conf.urls import handler404
handler404 = 'MLHealthAI.views.error_404_handler'
##
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.mainpage, name="main"),
    path('about/', views.about_page, name="about_page"),
    path('blog_single/', views.blog_single_page, name="blog_single_page"),
    path('blog/', views.blog_page, name="blog_page"),
    path('contact/', views.contact_page, name="contact_page"),
    path('portfolio/', views.portfolio_page, name="portfolio_page"),
    path('services/', views.services_page, name="services_page"),

    path('create/', views.create_contact,name="create_main_model"),
    path('contact/create/', views.create_contact,name="create_contact_model"),

    path('news/', views.create_newsletter, name="main_news"),
    path('about/news/', views.create_newsletter, name="about_news"),
    path('blog_single/news/', views.create_newsletter, name="blog_single_news"),
    path('blog/news/', views.create_newsletter, name="blog_news"),
    path('contact/news/', views.create_newsletter, name="contact_news"),
    path('portfolio/news/', views.create_newsletter, name="portfolio_news"),
    path('services/news/', views.create_newsletter, name="services_news"),
]
