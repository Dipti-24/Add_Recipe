from django.shortcuts import render,redirect
from django.http import HttpResponse
from .utils import send_email_to_client
#from home.models import Car
from vege.seed import*
from django.conf import settings
# Create your views h

def send_email(request):
    send_email_to_client()
    return redirect('/')


def home(request):
    #return HttpResponse("<h1>Django server<h1>")

    #Car.objects.create(car_name=f"Nexon-{random.randint(0 , 100)}")

    peoples=[
        {'name':'Divy','age':21},
        {'name':'Dipti','age':20},
        {'name':'Pukku','age':15},
    ]
    vegtable = ['pumpkin','tomato','potato']

    ''' text = """
      Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
""" '''
    return render(request,"home/index.html",context={'peoples':peoples ,'vegtable':vegtable,'page':'Django'})
def about(request):
    context={'page':'Home'}
    return render(request,"home/about.html",context)
def contact(request):
    context={'page':'Contact'}
    return render(request,"home/contact.html",context)



def sucess(request):
    return HttpResponse("hi")