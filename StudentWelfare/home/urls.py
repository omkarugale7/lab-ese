
from django.contrib import admin
from django.urls import path, include
from home import views
urlpatterns = [ 
    # path("", views.index,name='home'),
    path("", views.index,name='index'),
    path("about", views.about,name='about'),
    path("contact", views.contact,name='contact'),
    path("services", views.services,name='services'),
    path("scheme1", views.scheme1,name='scheme1'),
    path("scheme2", views.scheme2,name='scheme2'),
    path("scheme3", views.scheme3,name='scheme3'),  

    # path('admin/',admin.site.urls),
    # path('',include('home.urls'))
]