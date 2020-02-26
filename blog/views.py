from django.shortcuts import render
from blog.models import UserType

# Create your views here.

def index(request):
    return render(request, 'index.html')

def retrieveusertype(request):
    user_type= UserType.objects.all()