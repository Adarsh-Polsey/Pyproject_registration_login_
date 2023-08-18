from datetime import datetime

from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from myapp.models import *


def Login(request):
    return render(request,"Loginc.html")
def login_post(request):
    uname=request.POST['username']
    pswrd=request.POST['password']
    result=login.objects.filter(username=uname,password=pswrd)
    if result.exists():
        res=login.objects.get(username=uname,password=pswrd)
        request.session['lid']=res.id
        if res.user_type=="user":
            return HttpResponse('''<script>alert("Login success");window.location="/myapp/home/"</script>''')
        else:
            return HttpResponse('''<script>alert("Incorrect credentials");window.location="/myapp/login/"</script>''')
    else:
        return HttpResponse('''<script>alert("User type not found");window.location="/myapp/login/"</script>''')
def regi(request):
    return render(request,"registration.html")

def reg_post(request):
    name=request.POST['name']
    email=request.POST['email']
    number=request.POST['number']
    gender=request.POST['gender']
    district=request.POST['district']
    password=request.POST['password']
    c_password=request.POST['confirm']
    image = request.FILES['image']
    lobj=login()
    lobj.username=email
    lobj.password=c_password
    lobj.user_type="user"
    lobj.save()

    s = datetime.now().strftime("%Y%m%d-%H%M%S") + ".jpg"
    fs=FileSystemStorage()
    fn=fs.save(s,image)
    path=fs.url(s)
    robj=reg()
    robj.name=name
    robj.email=email
    robj.number=number
    robj.image=path
    robj.gender=gender
    robj.district=district
    robj.password=password
    robj.LOGIN=lobj
    robj.save()
    return HttpResponse('''<script>alert("Registration success");window.location="/myapp/login/"</script>''')

def home(request):
    return render(request,"home.html")

def view(request):
    result=reg.objects.get(LOGIN_id=request.session['lid'])
    return render(request,"view.html",{'data':result})

def cfunc(request):
    return render(request,'cmplaint.html')

def cpost(request):
    cmod=request.POST['complaint']
    cobj=complaint()
    cobj.complaint=cmod
    cobj.date=datetime.now()
    result=login.objects.get(id=request.session['lid'])
    res=reg.objects.get(LOGIN=result)
    cobj.REGISTRATION=res
    cobj.save()
    return HttpResponse('''<script>alert("complaint recorded successfully");window.location="/myapp/home/"</script>''')

def vcmp(request):
    result=login.objects.get(id=request.session['lid'])
    res=reg.objects.get(LOGIN=result)
    comp=complaint.objects.filter(REGISTRATION=res)
    return render(request,"vcmpl.html",{'data' : comp})