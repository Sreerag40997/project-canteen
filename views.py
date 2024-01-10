from typing import Type

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from myapp.models import *


def login(request):
    return render(request,'login_template.html')

def login_post(request):
    user=request.POST['username']
    password=request.POST['password']
    lobj=Login.objects.filter(Username=user,Password=password)
    if lobj.exists():
        lobj=Login.objects.get(Username=user,Password=password)
        request.session['lid']=lobj.id
        if lobj.Type=='admin':
            return HttpResponse('<script>alert("login successfully");window.location="/myapp/adminhomes/"</script>')
        else :
            return HttpResponse('<script>alert("admin not found");window.location="/myapp/loginn/"</script>')
    else :
        return HttpResponse('<script>alert("admin not found");window.location="/myapp/loginn/"</script>')

def changepassword(request):
    return render(request,'admin/change password.html')
def changepasswords_post(request):
    oldpassword = request.POST['username']
    newpassword = request.POST['password1']
    conformpassword = request.POST['password2']
    log=Login.objects.get(id=request.session['lid'])
    if log.Password == oldpassword:
        if newpassword==conformpassword:
            log2=Login.objects.filter(id=request.session['lid']).update(Password=conformpassword)
            return HttpResponse('<script>alert("password changed");window.location="/myapp/loginn/"</script>')
        else:
            return HttpResponse('<script>alert("password not change");window.location="/myapp/changepassword/"</script>')
    else:
        return HttpResponse('<script>alert("password not change");window.location="/myapp/changepassword/"</script>')


def addfoods(request):
     return render(request,'admin/add food.html')

def addfood_post(request):
    foodname=request.POST['name']
    type=request.POST['radio']
    discription=request.POST['discription']
    image=request.FILES['image']
    from django.core.files.storage import FileSystemStorage
    fs=FileSystemStorage()
    from datetime import datetime
    date=datetime.now().strftime('%Y%m%d-%H%M%S')+".jpg"
    fn=fs.save(date,image)

    price=request.POST['price']
    fobj=Food()
    fobj.Foodname=foodname
    fobj.Type=type
    fobj.Discription=discription
    fobj.Image=fs.url(date)
    fobj.Price=price


    fobj.save()
    return HttpResponse('<script>alert("Food Added Successfully");window.location="/myapp/adminhomes/"</script>')
def addstaffs(request):
    return render(request,'admin/add staff.html')

def addstaff_post(request):
    name=request.POST['name']
    dob=request.POST['date']
    gender=request.POST['textfield']
    phone=request.POST['phone']
    email=request.POST['email']
    housename=request.POST['house']
    place=request.POST['place']
    post=request.POST['post']
    pin=request.POST['pin']
    district=request.POST['district']
    state=request.POST['state']
    idproof=request.FILES['idproof']
    photo=  request.FILES['photo']

    from django.core.files.storage import FileSystemStorage
    fs = FileSystemStorage()
    from datetime import datetime
    date = datetime.now().strftime('%Y%m%d-%H%M%S') + ".jpg"
    fs.save(date, photo)
    path=fs.url(date)

    from django.core.files.storage import FileSystemStorage
    fs1 = FileSystemStorage()
    from datetime import datetime
    date1 = datetime.now().strftime('%Y%m%d-%H%M%S') + ".jpg"
    fs1.save(date1, idproof)
    path1=fs.url(date1)

    sobj=Staff()
    sobj.Name=name
    sobj.Dob=dob
    sobj.Gender=gender
    sobj.Phone=phone
    sobj.Email=email
    sobj.Housename=housename
    sobj.Place=place
    sobj.Post=post
    sobj.Pin=pin
    sobj.District=district
    sobj.State=state
    sobj.Idproof=path1
    sobj.Photo=path

    sobj.save()
    return HttpResponse('<script>alert("Staff Added Successfully");window.location="/myapp/addstaffs/"</script>')
def deletestaff(request,id):
    ref=Staff.objects.get(id=id).delete()
    return HttpResponse('<script>alert(" Delete Successfully");window.location="/myapp/staffviews/"</script>')
def editstaffs(request,id):
    res=Staff.objects.get(id=id)
    return render(request,'admin/edit staff.html',{'data':res})

def editstaff_post(request):
    did=request.POST['id1']
    name=request.POST['name']
    dob=request.POST['date']
    gender=request.POST['textfield']
    phone=request.POST['phone']
    email=request.POST['email']
    housename=request.POST['house']
    place=request.POST['place']
    post=request.POST['post']
    pin=request.POST['pin']
    district=request.POST['district']
    state=request.POST['state']
    if 'idproof' in request.FILES:
        idproof = request.FILES['idproof']
        if idproof!='':
            from django.core.files.storage import FileSystemStorage
            fs1 = FileSystemStorage()
            from datetime import datetime
            date1 = datetime.now().strftime('%Y%m%d-%H%M%S') + ".jpg"
            fn = fs1.save(date1, idproof)
            sobj = Staff.objects.get(id=did)
            sobj.Name = name
            sobj.Dob = dob
            sobj.Gender = gender
            sobj.Phone = phone
            sobj.Email = email
            sobj.Housename = housename
            sobj.Place = place
            sobj.Post = post
            sobj.Pin = pin
            sobj.District = district
            sobj.State = state
            sobj.Idproof = fs1.url(date1)

            sobj.save()
            return HttpResponse(
                '<script>alert("Staff Added Successfully");window.location="/myapp/addstaffs/"</script>')

    if 'photo' in request.FILES:
        photo = request.FILES['photo']
        if photo != '':
            from django.core.files.storage import FileSystemStorage
            fs = FileSystemStorage()
            from datetime import datetime
            date = datetime.now().strftime('%Y%m%d-%H%M%S') + ".jpg"
            fn = fs.save(date, photo)
            sobj = Staff.objects.get(id=did)
            sobj.Name = name
            sobj.Dob = dob
            sobj.Gender = gender
            sobj.Phone = phone
            sobj.Email = email
            sobj.Housename = housename
            sobj.Place = place
            sobj.Post = post
            sobj.Pin = pin
            sobj.District = district
            sobj.State = state
            sobj.Photo = fs.url(date)

            sobj.save()
            return HttpResponse(
                '<script>alert("Staff Added Successfully");window.location="/myapp/addstaffs/"</script>')
    else:
        sobj = Staff()
        sobj.Name = name
        sobj.Dob = dob
        sobj.Gender = gender
        sobj.Phone = phone
        sobj.Email = email
        sobj.Housename = housename
        sobj.Place = place
        sobj.Post = post
        sobj.Pin = pin
        sobj.District = district
        sobj.State = state

        sobj.save()
        return HttpResponse('<script>alert("Staff Added Successfully");window.location="/myapp/addstaffs/"</script>')

#
# def addtodaymenus(request):
#
#     return render(request,'admin/add today menu.html')
#
# def addtodaymenu_post(request):
#     food=request.POST['select1']
#     day=request.POST['select2']
#
#     mobj=Todaymenu()
#     mobj.Food=food
#     mobj.Day=day
#
#     mobj.save()
#     return HttpResponse("menu added")



def addtodaymenus(request):
    res=Food.objects.all()
    return render(request,'admin/add today menu.html',{'data':res})

def addtodaymenu_post(request):
    food=request.POST['select1']
    day=request.POST['select2']

    mobj=Todaymenu()
    mobj.FOOD_id=food
    mobj.Day=day

    mobj.save()
    return HttpResponse('<script>alert(" Added Successfully");window.location="/myapp/addtodaymenus/"</script>')


def addusers(request):
    return render(request,'admin/add user.html')

def addusers_post(request):
    username=request.POST['username']
    department=request.POST['department']
    year=request.POST['year']
    gender=request.POST['gender']
    dob=request.POST['dob']
    phone=request.POST['phone']
    email=request.POST['email']
    registerno=request.POST['register']
    admissionno=request.POST['admission']
    place=request.POST['place']
    post=request.POST['post']
    pin=request.POST['pin']
    district=request.POST['district']
    state=request.POST['state']
    idproof=request.POST['proof']
    photo=request.POST['photo']

    uobj = User()
    uobj.Name=username
    uobj.Dob = dob
    uobj.Gender = gender
    uobj.Phone = phone
    uobj.Email = email
    uobj.Admissionno =admissionno
    uobj.Place = place
    uobj.Post = post
    uobj.Pin = pin
    uobj.District = district
    uobj.State = state
    uobj.Idproof = idproof
    uobj.Registerno =registerno
    uobj.Department = department
    uobj.Year = year

    uobj.save()
    return HttpResponse("user added")

def viewsprecount(request):
    return render(request,'admin/precount view.html')
def billviews(request):
    res=Bill.objects.all()
    return render(request,'admin/view bill.html',{'data':res})
def foodviews(request):
    res=Food.objects.all()
    return render(request,'admin/view food.html',{'data':res})
def editfood(request,did):
    res=Food.objects.get(id=did)
    return render(request,'admin/edit food.html',{'data':res})
def editfood_post(request):
    did=request.POST['id1']
    foodname=request.POST['name']
    type=request.POST['radio']
    discription=request.POST['discription']



    price=request.POST['price']
    if 'image' in request.FILES:
        image = request.FILES['image']
        if image!='':
            from django.core.files.storage import FileSystemStorage
            fs = FileSystemStorage()
            from datetime import datetime
            date = datetime.now().strftime('%Y%m%d-%H%M%S') + ".jpg"
            fn = fs.save(date, image)
            fobj = Food.objects.get(id=did)


            fobj.Foodname = foodname
            fobj.Type = type
            fobj.Discription = discription
            fobj.Image = fs.url(date)
            fobj.Price = price

            fobj.save()
            return HttpResponse(
                '<script>alert("Food Added Successfully");window.location="/myapp/adminhomes/"</script>')
    else:

        fobj=Food.objects.get(id=did)

        fobj.Foodname=foodname
        fobj.Type=type
        fobj.Discription=discription
        fobj.Price=price


        fobj.save()
        return HttpResponse('<script>alert(" Edited Successfully");window.location="/myapp/foodviews/"</script>')
def deletefood(request,id):
    ref=Food.objects.get(id=id).delete()
    return HttpResponse('<script>alert(" Delete Successfully");window.location="/myapp/foodviews/"</script>')
def orderhistoryviews(request):
    obj=Ordermain.objects.all()
    return render(request,'admin/view order history.html',{"data":obj})
def viewordermore(request,id):
    obj = Ordersub.objects.filter(ORDERMAIN=id)
    return render(request, 'admin/view ordermore.html', {"data": obj})
def orderhistoryviews_post(request):
    fromsearch=request.POST['search1']
    tosearch=request.POST['search2']
    return HttpResponse("search successfully")
def staffviews(request):
    res=Staff.objects.all()
    return render(request,'admin/view staff.html',{'data':res})

def staffviews_post(request):
    search=request.POST['search1']
    return  HttpResponse("succeessfully")





def todaymenueviews(request):
    res=Todaymenu.objects.all()
    return render(request,'admin/view today menu.html',{'data':res})

def  todaymenueviews_post(request):
    search=request.POST['search1']
    res=Todaymenu.objects.filter(FOOD__Foodname__icontains=search)

    return render(request,'admin/view today menu.html',{'data':res})
def delete_todaysmenu(request,id):
    ref =Todaymenu.objects.get(id=id)
    ref.delete()
    return HttpResponse('<script>alert(" Delete Successfully");window.location="/myapp/todaymenueviews/"</script>')

def usersview(request):
    res = User.objects.all()
    return render(request,'admin/view user.html',{'data':res})

def usersview_post(request):

    search=search=request.POST['search1']
    return HttpResponse('successfully')
def adminhomes(request):
    return render(request,'admin/admin home template.html')
def index(request):
    return render(request,'admin/index.html')



##################33user

def user_login(request):
    username=request.POST['username']
    password=request.POST['password']
    return JsonResponse({'status':'ok'})

def user_changepassword(request):
    oldpassword=request.POST['oldpassword']
    newpassword=request.POST['']
    return JsonResponse({'status':'ok'})

