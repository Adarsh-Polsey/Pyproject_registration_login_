from datetime import datetime

from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from myapp.models import *


def Login(request):
    return render(request,"login.html")
def login_post(request):
    uname=request.POST['username']
    pswrd=request.POST['password']
    result=login.objects.filter(username=uname,password=pswrd)
    if result.exists():
        res=login.objects.get(username=uname,password=pswrd)
        if res.user_type=="user":
            return HttpResponse('''<script>alert("Login success");windows.location="/myapp/home/"</script>''')
        else:
            return HttpResponse('''<script>alert("Incorrect credentials");windows.location="/myapp/login/"</script>''')
    else:
        return HttpResponse('''<script>alert("User type not found");windows.location="/myapp/login/"</script>''')
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
    return HttpResponse('''<script>alert("Registration success");windows.location="/myapp/login/"</script>''')

def home(request):
    return render(request,"home.html")