#from django.urls import path
#from . import views

#urlpatterns=[
    
   # path('test/', views.about, name='test'),
    #path('Login/', views.Login , name='Login'),
    #path('register/', views.register , name='register'),
    #path('profile/', views.profile , name='profile'),
    #path('vehicles/', views.vehicles , name='vehicles'),
    #path('available_vehicles/', views.available_vehicles, name='available_vehicles'),
    #path('location/', views.location , name="location"),
    #path('logout/', views.logoutuser, name='logout')

#]

from django.urls import path
from . import views
urlpatterns =[
     path('home/', views.Homepage, name='home-page'),
     path('register/', views.register, name='register-page'),
     path('login/', views.Login, name='login-page'),
     path('logout/', views.logoutuser, name='logout'),
     path('make_payment/', views.make_payment , name='make_payment' ),
     path('book_vehicle/', views.book_vehicle , name='book_vehicle'),
     path('vehicles/', views.vehicles, name='vehicles'),
     path('landing_page/', views.landing_page, name='landing_page'),
     path('update_database/', views.update_database, name='update_database'),
     path('return_vehicle/', views.return_vehicle, name='return_vehicle'),

]