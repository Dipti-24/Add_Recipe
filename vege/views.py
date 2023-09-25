from django.shortcuts import render,redirect
from .models import*
from django.http import HttpResponse
#from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
import math
'''from django.contrib.auth import get_user_model

User=get_user_model()'''

# Create your views here.
@login_required(login_url="/login/")
def receips(request):
    if request.method=="POST":
        data=request.POST
        re_name=data.get('re_name')
        re_des=data.get('re_des')
        re_image=request.FILES.get('re_image')
        #print(re_name)
        #print(re_des)
        #print(re_image)
        Recipe.objects.create(
            re_name=re_name,
            re_des=re_des,
            re_image=re_image,
        )
        return redirect('/receips/')
    
    queryset=Recipe.objects.all()
    if request.GET.get('search'):
        #print(request.GET.get('search'))
        queryset=queryset.filter(re_name__icontains=request.GET.get('search'))

    context={'receips':queryset}

    return render(request,'receips.html',context)

def update_rec(request,id):
    queryset=Recipe.objects.get(id=id)
    if request.method=="POST":
        data=request.POST
        re_name=data.get('re_name')
        re_des=data.get('re_des')
        re_image=request.FILES.get('re_image')
        queryset.re_name=re_name
        queryset.re_des=re_des

        if re_image:
            queryset.re_image=re_image
        queryset.save()
        return redirect('/receips/')
    context={'receips':queryset}
    return render(request,'update.html',context)

def del_rec(request,id):
    #print(id)
    queryset=Recipe.objects.get(id=id)
    queryset.delete()
    return redirect('/receips/')


def login_pg(request):
    if request.method=="POST": 
        username=request.POST.get('username')
        password=request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            messages.error(request,'invalid name')
            return redirect('/login/')
        
        user=authenticate(username=username,password=password)

        if user is None:
            messages.error(request,'invalid password')
            return redirect('/login/')
        
        else:
            login(request,user)
            return redirect('/receips/')

    return render(request,'login.html')

def logout_pg(request):
    logout(request)
    return redirect('/login/')

def register_pg(request):
    if request.method=="POST":
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=User.objects.filter(username=username)

        if user.exists():
            messages.info(request,'username already taken')
            return redirect('/register/')

        user=User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username

        )
        user.set_password(password)
        user.save()

        messages.info(request,'account created')

        return redirect('/register/')
    
    
    return render(request,'register.html')


from django.db.models import Q,Sum


def get_students(request):
    queryset=Student.objects.all()
    search=""
    
    #contact_list = Contact.objects.all()

    if request.GET.get('search'):
        search=request.GET.get('search')
        queryset=queryset.filter(Q(student_name__icontains=search) | Q(department__department__icontains=search)|
         Q(student_age__icontains=search))

    paginator = Paginator(queryset,30)  # Show 30 contacts per page.

    page_number = request.GET.get("page")
    context = {
        'queryset': queryset
    }
    page_obj = paginator.get_page(page_number)  
    a=math.ceil(len(queryset)/10)
    page_number=paginator.get_page(page_number)




    #print(page_obj)
    return render(request,'report/student.html',{'queryset':page_obj,"range":range(a),"search":search})

from .seed import generate_report_card

def see_marks(request,student_id):
    #generate_report_card()
    queryset=SubjectMarks.objects.filter(student__student_id__student_id=student_id)
    total_marks=queryset.aggregate(total_marks=Sum("marks"))
    '''current_rank=-1
    ranks=Student.objects.annotate(marks=Sum("studentmarks__marks")).order_by('-marks','-student_age')
    j=1
    for rank in ranks:
        if student_id==rank.student_id.student_id:
            current_rank=j
            break
        j=j+1'''
    return render(request,'report/see_marks.html',{'queryset':queryset,'total_marks':total_marks})

# views.py
