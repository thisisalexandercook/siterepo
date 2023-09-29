from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate
from django.contrib import messages
from django.conf import settings
from .models import *

# Create your views here.
def home(request):
    return render(request, 'index.html')

def register(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        psw = request.POST["password"]

        user = User.objects.create_user(username=name, email=email, password=psw)
        user.first_name = name
        user.save()
        messages.success(request, "User registered successfully.")
        return redirect("login")
    return render(request, "registration.html")


def login(request):
    if request.method == "POST":
        name = request.POST["name"]
        psw = request.POST["password"]

        user = authenticate(username=name, password=psw)
        if user.is_authenticated:
            auth_login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("login")
    return render(request, "login.html", {})


def viewOrders(request):
    if not request.user.is_authenticated:
            return redirect('login')

    orders = Booking.objects.filter(user=request.user)
    return render(request, "vieworders.html", {"orders": orders})


def logout(request):
    auth_logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("login")


def about_us(request):
    return render(request, 'about.html')


def accomodation(request):
    rooms = Room.objects.filter(available=True)
    print("==>>> Rooms : ",rooms)
    return render(request, 'accomodation.html', {'rooms': rooms})


def gallery(request):
    g_objs = Gallery.objects.all()
    return render(request, 'gallery.html', {'gallery':g_objs})


def blog(request):
    return render(request, 'blog.html')


def contact(request):
    return render(request, 'contact.html')


def info(request, id):

    # try:
    if id != 0:
        room_obj = Room.objects.filter(id=id)
    else:
        room_obj = Room.objects.all()

    if request.method == "POST":
        fname = request.POST.get("f_name")
        lname = request.POST.get("l_name")
        phone = request.POST.get("contact")
        room = request.POST.get("rtype")
        persons = request.POST.get("adults")
        child = request.POST.get("childs")
        a_date = request.POST.get("a_date")
        d_date = request.POST.get("d_date")
        address = request.POST.get("address")
        email = request.POST.get("email")


        b = Booking.objects.create(user=request.user,fname=fname,lname=lname,phone=phone,Address=address,room=room_obj,persons=persons,child=child,a_date=a_date,d_date=d_date,email=email)
        context = {"oid": b.id, "key": settings.STRIPE_PUBLISHABLE_KEY}
        return render(request, "payment.html")
    # except Exception as e:
    #     print("Something wrong")
    return render(request, "order.html", {'room': room_obj, 'id' : id})



def orderPlaced(request):
    return render(request, "orderplaced.html", {})
