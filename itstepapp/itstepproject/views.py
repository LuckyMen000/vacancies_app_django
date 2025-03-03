from django.shortcuts import render
from .models import Category, Job

def home_page(request):
    categories = Category.objects.all()
    jobs = Job.objects.all()

    context = {
        'categories': categories,
        'jobs': jobs
    }
    return render(request, "home.html", context )

def about_page(request):
    return render(request, "about.html")

def contact_page(request):
    return render(request, "contact.html")