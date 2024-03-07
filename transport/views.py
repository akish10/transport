
"""from django.shortcuts import render, redirect

import re
#from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from .models import * #Vehicle, Register

#check password and validate login
from django.contrib.auth.hashers import check_password
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Register, Login
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.
#@login_required()


def test(request):

    return render(request,'test.html')


def profile(request):

    return render(request, 'profile.html')


def Login(request):

    if request.method == 'POST':
        user_name = request.POST.get('username')
        password = request.POST.get('password')

        try:

            login_record = Login.objects.get(user_name=username)

            register_record = login_record.related_model


            if check_password(password, login_record.password):

                return redirect('profile')

            else:
                
                message.error(request,'invalid username or password')
                
                return redirect('Login')

        except ObjectDoesNotExist:

            message.error(request, 'invalid username or password')

        return redirect('profile')

    else:
        
        return render(request, 'login.html')


def register(request):

    if request.method == 'POST':

        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        user_name = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if len(password) < 9:
            
           return HttpResponse("Password must be at least 9 characters long")
            
        elif not re.search("[\W]", password):

            message = "Password must contain at least one special character"
            return render(request, 'register.html', {'message' : message})

    

        registration = Register.objects.create(
             first_name = first_name,
             last_name = last_name,
             user_name = user_name,
             email = email,
             password =password
             )

        return redirect('Login')

        
        #registration= Register(first_name = first_name,last_name=last_name,User_name=User_name,Email=Email)

        #registration.save()



    return render(request, 'register.html')


#def truck(request):
    #available_vehicles = Vehicle.objects.all()

    #vehicles_list = [{'Vehicle_id':vehicle.Vehicle_id, 'Capacity':vehicle.Capacity,'Type':vehicle.Type,'refrigerated':vehicle.refrigerated} for vehicle in available_vehicles]
    
    
    
    #return JsonResponse({'vehicles': vehicles_list})

    #return render(request, 'truck.html')

def available_vehicles(request):

    #available_vehicles = Vehicle.objects.all()

    #vehicles_list = [{'Vehicle_id':vehicle.Vehicle_id, 'Capacity':vehicle.Capacity , 'Type':vehicle.Type ,'refrigerated':vehicle.refrigerated} for vehicle in available_vehicles]
    #return JsonResponse({'vehicles': vehicles_list})
    #vehicles=Vehicle.objects.all()

    return render(request,'vehicles.html', {'vehicles':vehicles})




def vehicles(request):
    available_vehicles = Vehicle.objects.all()
    vehicles_list = [{'Vehicle_id':vehicle.Vehicle_id,'Capacity':vehicle.Capacity ,'Type':vehicle.Type ,'refrigerated':vehicle.refrigerated} for vehicle in available_vehicles]
    #return JsonResponse({'vehicles': vehicles_list})
    return render(request, 'truck.html',{'vehicles_list':vehicles_list} )
"""


from django.shortcuts import render, redirect

from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login, logout

from django.http import HttpResponse,JsonResponse

from django.contrib.auth.decorators import login_required

from .models import * 

from django.views.decorators.csrf import csrf_exempt

import json  


# Create your views here.

@login_required()

def Homepage(request):

    username = request.user.username

    return render(request, 'index.html', {'username': username})


def register(request):

    if request.method == 'POST':

        fname = request.POST.get('fname')

        lname = request.POST.get('lname')

        name = request.POST.get('uname')

        email = request.POST.get('email')

        password = request.POST.get('pass')

        new_user = User.objects.create_user(name, email, password)

        new_user.first_name = fname

        new_user.last_name = lname

        new_user.save()

        return redirect('login-page')

    return render(request, 'register.html', {})


def Login(request):

    if request.method == 'POST':

        password = request.POST.get('pass')

        name = request.POST.get('uname')

        user = authenticate(request, username=name, password=password)

        if user is not None:

            login(request, user)

            return redirect('home-page')

        else:

            return HttpResponse('Error,User Does not Exist')

    else:

        return render(request, 'login.html', {})



def logoutuser(request):

    logout(request)

    return redirect('login-page')



def vehicles(request):

    available_vehicles = Vehicle.objects.all()

    vehicles_list = [{'Vehicle_id':vehicle.Vehicle_id,'Capacity':vehicle.Capacity ,'Type':vehicle.Type ,'refrigerated':vehicle.refrigerated } for vehicle in available_vehicles]

    return render(request,'vehicles.html',{'vehicles_list':vehicles_list} )


def book_vehicle(request):

    if request.method == 'POST':

        product = request.POST.get('product')

        perishable = request.POST.get('type') == 'on'

        quantity = request.POST.get('quantity')

        pickup = request.POST.get('pickup')

        destination = request.POST.get('destination')


        book = Book.objects.create(
            product=product,
            perishable=perishable,
            quantity=quantity,
            pickup=pickup,
            destination=destination,
            
        )

        book.save()

        return redirect('make_payment')


    

    return render(request, 'book.html')
    


def landing_page(request):

    return render(request, 'landing.html')




@csrf_exempt
def make_payment(request):

    if request.method == 'POST':
        
        Vehicle_id = request.POST.get('Vehicle_id')

        amount = request.POST.get('amount')

        cardholder = request.POST.get('cardholder')

        card_number = request.POST.get('cardnumber')

        expiry_date = request.POST.get('expiry')

        cvc = request.POST.get('cvc')

        try:
            
            payment = Payment.objects.create(
                Vehicle_id=Vehicle_id,
                amount=amount,
                card_number= card_number,
                cardholder=cardholder,
                expiry_date = expiry_date,
                cvc= cvc,
                
                
            )

            payment.save()
            
            
            vehicle = Vehicle.objects.get(Vehicle_id=Vehicle_id)

            vehicle.delete()
            
            vehicle.save()

         
         
            return HttpResponse( 'Payment successful')

        

        except Exception as e:

            return JsonResponse({'error': str(e)}, status=500)


    return render(request,'pay.html')

@csrf_exempt
def update_database(request):

    if request.method == 'POST':

        data = json.loads(request.body)

        vehicle_id = data.get('Vehicle_id')

        try:
            
            return HttpResponse( 'Database updated successfully')

        except Exception as e:

            return JsonResponse({'error': str(e)}, status=500)

    else:
        return HttpResponse('Only POST requests are allowed', status=405)



#return vehicle

@csrf_exempt
def return_vehicle(request):

    if request.method == 'POST':
       
        vehicle_id = request.POST.get('Vehicle_id')

        try:
            
            vehicle = Vehicle.objects.get(Vehicle_id=vehicle_id)
            
            
            vehicle.save()


            request.user.vehicle_returned = True

            request.user.save()



            return HttpResponse('Vehicle returned successfully', status=200)
        
        except Vehicle.DoesNotExist:

            return HttpResponse('Vehicle not found', status=404)
        
        except Exception as e:

            return JsonResponse({'error': str(e)}, status=500)

    else:
        
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)