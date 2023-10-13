from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Employee
# Create your views here.

def Dashboard(request):
    if('email' in request.session ):
        data = Employee.objects.all()
        print("data")
        print(request.session['email'])
        return render(request,'Dashboard.html',{"data":data})
    else:
        return redirect(Login)

def Login(request):
    if(request.method == 'GET'):
        return render(request,'Login.html',{})
    else:
        email = request.POST['email']
        password = request.POST['password']
        try:
            emp = Employee.objects.get(email = email,password=password)
            request.session['email'] = email
            return redirect(Dashboard)
        except:
            msg = 'Plz enter valid details...'
            return render(request,'Login.html',{'msg':msg})
def Signup(request):
    if(request.method == 'GET'):
        return render(request,'Homepage.html',{})
    else:
        ename = request.POST["ename"]
        print(ename)
        email = request.POST['email']
        Birth_date = request.POST['dob']
        gender = request.POST['gender']
        education = request.POST['education']
        password = request.POST['password']
        data = Employee()
        data.ename = ename
        data.email = email
        data.Birth_date = Birth_date
        data.gender = gender
        data.education = education
        data.password = password
        data.save()
        return redirect(Login)
def Edit(request):
    id = request.POST['empid']
    ename = request.POST["ename"]
    print(ename)
    email = request.POST['email']
    Birth_date = request.POST['dob']
    gender = request.POST['gender']
    education = request.POST['education']
    password = request.POST['password']
    data = Employee.objects.get(id = id)
    data.ename = ename
    data.email = email
    data.Birth_date = Birth_date
    data.gender = gender
    data.education = education
    data.password = password
    data.save()
    return redirect(Dashboard)

def Remove(request):
    id = request.GET['empid']
    emp = Employee.objects.get(id=id)
    emp.delete()
    return redirect(Dashboard)
def Logout(request):
    print(request.session['email'])
    request.session.clear()
    
    print("\n\n\n logout:",request.session.get('email'))
    return redirect(Login)