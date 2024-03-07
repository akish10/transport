"""
URL configuration for Transport project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path 
from transport import views

#urlpatterns=[
   # path('admin/', admin.site.urls),
    #path('', views.test),
    #path('Login/', views.Login , name='Login'),
    #path('register/', views.register , name='register'),
    #path('profile/', views.profile ),
    #path('vehicles/', views.vehicles, name='vehicles'),
    #path('available_vehicles/', views.available_vehicles),
    
    #path('location/', views.location , name="location"),
    #path('logout/', views.logoutuser, name='logout')

#]
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.landing_page),
    path('home/', views.Homepage),
    path('register/',views.register),
    path('login/', views.Login),
    path('logout/',views.logoutuser),
    path('make_payment/', views.make_payment),
    path('book_vehicle/', views.book_vehicle),
    path('vehicles/', views.vehicles),
    path('update_database/', views.update_database),
    path('return_vehicle/', views.return_vehicle),
    #path('', include('movers.urls')),
]
