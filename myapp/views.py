from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from myapp.models import *


def new(request):
    return render(request,"login.html")
def login_post(request):
    username=request.POST["username"]
    print(username)
    password=request.POST["password"]
    print(password)
    lobj=login()
    lobj.username=username
    lobj.password=password
    lobj.save()
    return render(request,"viewlogin.html",{'username':username,'password':password})
    return HttpResponse("OK")

def view_login(request):
    result=login.objects.all()
    return render(request,"viewlogin.html",{'data':result})

def regi(request):
    return render(request,"registration.html")

def regi_post(request):
    name=request.POST['name1']
    email=request.POST["email"]
    number=request.POST["number"]
    gender=request.POST["gender"]
    district=request.POST["district"]
    password=request.POST["password"]
    cnfrm_pswd=request.POST["confirm"]
    robj=reg()
    robj.name=name
    robj.email=email
    robj.number=number
    robj.gender=gender
    robj.district=district
    robj.password=password
    robj.cnfrm_pswd=cnfrm_pswd
    robj.save()
    return HttpResponse("Success")
def view_reg(request):
    ans=reg.objects.all()
    return render(request,"viewreg.html",{'data':ans})

def edit_reg(request,id):
    result=reg.objects.get(id=id)
    return render(request,"editreg.html",{'data':result,"id":id})

def edit_post(request):
    id=request.POST['id']
    name=request.POST['name1']
    email=request.POST["email"]
    number=request.POST["number"]
    gender=request.POST["gender"]
    district=request.POST["district"]
    password=request.POST["password"]
    cnfrm_pswd=request.POST["confirm"]
    result=reg.objects.filter(id=id).update(name=name,email=email,number=number,gender=gender,district=district,password=password,cnfrm_pswd=cnfrm_pswd)
    return HttpResponse("Edit Success")

def delete(request,id):
    result=reg.objects.filter(id=id).delete()
    return HttpResponse('''<script>alert("Deletion success");window.location="/myapp/viewreg/"</script>''')
