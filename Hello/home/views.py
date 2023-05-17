from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages
from .forms import usersForm

# Create your views here.
def index(request):
    messages.success(request,'This is root page')
    return render(request,"index.html")

def about(request):
    d={
        'title':'Gangesh',
        'clist':[1,2,3,4],
        'student_details':[
            {'name':'pardeep','phone':12344},
            {'name':'Amit','phone':95543}
        ]
    }
    return render(request,"about.html",d)

def services(request):
    return render(request,"services.html")

# def index(request):
#     return render(request,".html")
# def about(request):
#     return HttpResponse("this is About")
def contact(request):
    if request.method=="POST":
        n=request.POST.get('name1')
        e=request.POST.get('email')
        g=request.POST.get("gender")
        d=request.POST.get('desc')
        con=Contact(name=n,email=e,gender=g,desc=d,date=datetime.today())
        con.save()
        messages.success(request,'Your message has been sent')
    return render(request,"contact.html")


def userForm(request):
    finalans=0
    fn=usersForm
def calculator(request):
    c=''
    try:
        if request.method=="POST":
            n1=eval(request.POST.get('value1'))
            n2=eval(request.POST.get('value2'))
            opr=request.POST.get('opr')
            if opr=="+":
                c=n1+n2
            elif opr=="-":
                c=n1-n2
            elif opr=='*':
                c=n1*n2
            else:
                c=n1/n2
    except:
        c="Invalid opr..... "
    print(c)            
    return render(request,"calculator.html",{'c':c})

def even_odd(request):
    c=''
    
    if request.method=="POST":
        if request.POST.get('num1')=="":
            return render(request,'odd_even.html',{'error':True})
        n1=eval(request.POST.get('value'))
        if n1%2==0:
            c='Even number'
        else:
            c='Odd number'

    return render(request,'odd_even.html',{'c':c})



