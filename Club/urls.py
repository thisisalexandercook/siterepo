from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('register/', register, name='register'),
    path('about_us/', about_us, name='about_us'),
    path('accomodation/', accomodation, name='accomodation'),
    path('gallery/', gallery, name='gallery'),
    path('blog/', blog, name='blog'),
    path('contact/', contact, name='contact'),
    path('info/<int:id>/', info, name='info'),
    path("order/", orderPlaced, name="orderplaced"),
    path("vieworder/", viewOrders, name="vieworder"),
]