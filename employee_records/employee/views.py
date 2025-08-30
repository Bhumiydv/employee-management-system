from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required
from .models import *

# Create your views here.
def index(request):
    return render(request,'index.html')

def login(request):
    error=''
    if request.method == 'POST':
        u=request.POST['uname']
        p=request.POST['pass']
        admin=auth.authenticate(username=u,password=p)
        try:
            if admin.is_staff:
                auth.login(request,admin)
                error='no'
            else:
                error='yes'
        except:
            error='yes'
    d={'error':error}
    return render(request,'login.html',d)

def feedback(request):
    error=""
    if request.method == "POST":
        f = request.POST['fname']
        e = request.POST['email']
        m = request.POST['message']
        try:
            feedbackus.objects.create(fname=f,email=e,message=m)
            error = "no"
        except:
            error = "yes"
    d={'error':error}
    return render(request,'feedback.html',d)

@login_required(login_url='login')
def admin_home(request):
    return render(request,'admin_dashboard.html')

@login_required(login_url='login')
def add_employee(request):
    error = ""
    if request.method == "POST":
        id=request.POST['emp_id']
        f=request.POST['fname']
        l=request.POST['lname']
        dep=request.POST['Department']
        e=request.POST['email']
        m=request.POST['phone']
        c=request.POST['country']
        s=request.POST['state']
        city=request.POST['city']
        bd=request.POST['dob']
        jd=request.POST['doj']
        add=request.POST['Address']
        pswd=request.POST['pass']
        cpswd=request.POST['con_pass']
        img=request.FILES['image']
        try:
            employee.objects.create(empid=id,fname=f,lname=l,dep=dep,email=e,phone=m,country=c,state=s,city=city,dob=bd,doj=jd,address=add,password=pswd,con_password=cpswd,image=img)
            error='no'
        except:
            error='yes'
    d={'error':error}
    return render(request,'add_employee.html',d)

@login_required(login_url='login')
def view_records(request):
    data= employee.objects.all()
    d={'data':data}
    return render(request,'view_records.html',d)

@login_required(login_url='login')
def account(request):
    return render(request,'account.html')

@login_required(login_url='login')
def change_pass(request):
    if request.method == "POST":
        op=request.POST['cp']
        np=request.POST['np']
        user=request.user
        if not user.check_password(op):
            return redirect('change_pass')
        user.set_password(np)
        user.save()
    return redirect('login')

@login_required(login_url='login')
def Logout(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def edit_records(request,id):
    data=employee.objects.get(id=id)
    error=''
    if request.method == "POST":
        i=request.POST['emp_id']
        f=request.POST['fname']
        l=request.POST['lname']
        dep=request.POST['Department']
        e=request.POST['email']
        m=request.POST['phone']
        c=request.POST['country']
        s=request.POST['state']
        city=request.POST['city']
        bd=request.POST['dob']
        jd=request.POST['doj']
        add=request.POST['Address']
        pswd=request.POST['pass']
        con_pswd=request.POST['con_pass']
        p=request.FILES['image']

        data.empid=i
        data.fname=f
        data.lname=l
        data.dep=dep
        data.email=e
        data.phone=m
        data.country=c
        data.state=s
        data.city=city
        data.dob=bd
        data.doj=jd
        data.address=add
        data.password=pswd
        data.con_password=con_pswd
        data.image=p
        try:
            data.save()
            error='no'
        except:
            error='yes'
    d={'data':data,'error':error}
    return render(request,'edit_records.html',d)

@login_required(login_url='login')
def del_records(request,id):
    if request.method == "POST":
        data=employee.objects.get(id=id)
        data.delete()
    return redirect("view_records")

@login_required(login_url='login')
def search(request):
    return render(request,'search_records.html')

@login_required(login_url='login')
def search_emp(request):
    n=request.POST['sname']
    data=employee.objects.filter(fname__icontains=n)
    d={'data':data}
    return render(request,'view_records.html',d)

@login_required(login_url='login')
def view_feedbacks(request):
    data=feedbackus.objects.all()
    d={'data':data}
    return render(request,'view_feedbacks.html',d)

@login_required(login_url='login')
def del_feedbacks(request,id):
    if request.method == "POST":
        data=feedbackus.objects.get(id=id)
        data.delete()
    return redirect("view_feedbacks")