from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    # return HttpResponse("Hello, welcome to my Django app!")
    return render(request, 'home.html')

# Create your views here.
