from django.shortcuts import render
from . models import Company
from blog.models import UserType,Company

# Create your views here.

def index(request):
    return render(request, 'index.html')

def retrieveusertype(request):
    user_type = UserType.objects.all()

def company_info(request):
    if request.method =='POST':
        print(request.POST)
        comp = Company(company_name = request.POST['company_name'],
                       company_owner = request.POST['company_owner'],
                       company_domain = request.POST['company_domain'],
                       company_website = request.POST['company_website'],
                       company_size = request.POST['company_size'],
                       company_headquarters = request.POST['company_headquarters'],
                       company_type = request.POST['company_type'],
                       company_establishmentyear = request.POST['company_establishmentyear'],
                       company_specialties = request.POST['company_specialties'],
                       company_locations = request.POST['company_locations'])
        comp.save()

    return render(request,'company.html')

