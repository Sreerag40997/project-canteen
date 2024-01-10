from django.db import models

# Create your models here.
class Login(models.Model):
    Username=models.CharField(max_length=100)
    Password=models.CharField(max_length=100)
    Type=models.CharField(max_length=100)

class User(models.Model):
    LOGIN=models.ForeignKey(Login,on_delete=models.CASCADE)
    Username = models.CharField(max_length=100)
    Department= models.CharField(max_length=100)
    Year= models.CharField(max_length=100)
    Gender = models.CharField(max_length=100)
    Dob = models.CharField(max_length=100)
    Phone = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    Registerno = models.CharField(max_length=100)
    Addmissionno = models.CharField(max_length=100)
    Place = models.CharField(max_length=100)
    Post = models.CharField(max_length=100)
    Pin = models.CharField(max_length=100)
    District = models.CharField(max_length=100)
    State = models.CharField(max_length=100)
    Idproof = models.CharField(max_length=100)
    Photo = models.CharField(max_length=100)

class Staff(models.Model):
    Name = models.CharField(max_length=100)
    Gender = models.CharField(max_length=100)
    Dob = models.CharField(max_length=100)
    Phone = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    Housename = models.CharField(max_length=100)
    Place = models.CharField(max_length=100)
    Post = models.CharField(max_length=100)
    Pin = models.CharField(max_length=100)
    District = models.CharField(max_length=100)
    State = models.CharField(max_length=100)
    Idproof = models.CharField(max_length=100)
    Photo = models.CharField(max_length=100)

class Food(models.Model):
    Foodname = models.CharField(max_length=100)
    Type = models.CharField(max_length=100)
    Discription = models.CharField(max_length=100)
    Image = models.CharField(max_length=100)
    Price = models.CharField(max_length=100)

class Todaymenu(models.Model):
    FOOD=models.ForeignKey(Food,on_delete=models.CASCADE)
    # Food = models.CharField(max_length=100)
    Day = models.CharField(max_length=100)

class Precount(models.Model):
    USER = models.ForeignKey(User, on_delete=models.CASCADE)
    Date = models.CharField(max_length=100)
    Time = models.CharField(max_length=100)
    User = models.CharField(max_length=100)
    Type = models.CharField(max_length=100)


class Bill(models.Model):
    USER = models.ForeignKey(User, on_delete=models.CASCADE)
    TODAYSMENUE = models.ForeignKey(Todaymenu, on_delete=models.CASCADE)
    Date = models.CharField(max_length=100)
    Time = models.CharField(max_length=100)
    Type = models.CharField(max_length=100)
    Paymentstatus = models.CharField(max_length=100)
    Amount = models.CharField(max_length=100)
    Totalamount = models.CharField(max_length=100)

class Ordermain(models.Model):
    USER = models.ForeignKey(User, on_delete=models.CASCADE)
    Date = models.CharField(max_length=100)
    Time = models.CharField(max_length=100)
    Type = models.CharField(max_length=100)
    User= models.CharField(max_length=100)
    Status = models.CharField(max_length=100)
    Amount = models.CharField(max_length=100)

class Ordersub(models.Model):
   ORDERMAIN = models.ForeignKey(Ordermain, on_delete=models.CASCADE)
   TODAYSMENUS= models.ForeignKey(Todaymenu, on_delete=models.CASCADE)
   Quantity= models.CharField(max_length=100)

class Preorder(models.Model):
    USER = models.ForeignKey(User, on_delete=models.CASCADE)
    Date = models.CharField(max_length=100)
    Name = models.CharField(max_length=100)
    Time = models.CharField(max_length=100)
    Type = models.CharField(max_length=100)
