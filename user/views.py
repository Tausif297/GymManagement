from user.models import Plans
from django.shortcuts import redirect, render, HttpResponse
from .models import Contact, Plans, Member
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def index(request):
    plans = Plans.objects.all()
    count_1 = Member.objects.all().count()
    count_2 = Contact.objects.all().count()
    count_3 = Plans.objects.all().count()
    if request.method=="POST":
        name=request.POST.get('name')
        number=request.POST.get('number')
        message=request.POST.get('message')
        if len(number) !=10:
            messages.error(request,"Please enter 10 digit valid number")
        else:
            contact=Contact(name=name,number=number,message=message)
            contact.save()
            messages.success(request,"Your message has been sent.")
    return render(request,'index.html',{'plans': plans,'count_1':count_1,'count_2':count_2,'count_3':count_3})

def membership(request):
    if request.method=="POST":
        username = request.POST.get('username')
        contact_0 = request.POST.get('contact')
        contact_2 = request.POST.get('another_contact')
        email = request.POST.get('email')
        plans = request.POST.get('plans')

        if len(contact_0) !=10:
            messages.error(request,"Please enter 10 digit valid number")
        else:
            member=Member(username=username,contact_1=contact_0,contact_2=contact_2,email=email,plans=plans)
            member.save()
            messages.success(request,"Congrats You Are Now A Member Of Fitness Zone")
            return redirect('/')

    return render(request, 'membership.html')

def dashboard(request):
    count_1 = Member.objects.all().count()
    count_2 = Contact.objects.all().count()
    count_3 = Plans.objects.all().count()
    return render(request,'dashboard.html',{'count_1':count_1,'count_2':count_2,'count_3':count_3})

def Userlogin(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            if user.last_name != "Agent":
                login(request,user)
                messages.success(request,"Successfully logged in")
                return redirect('/')
        else:
            messages.success(request,"Incorrect Data ! please try again")
            return redirect('/login')
    messages.success(request,"You must login as a User")
    return redirect("/login")