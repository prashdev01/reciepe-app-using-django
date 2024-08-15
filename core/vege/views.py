from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import *
from django.contrib import messages
# Create your views here.




def recipies(request):
    if request.method == 'POST':
        data = request.POST
        reciepe_image =  request.FILES.get('reciepe_image')
        reciepe_name =  data.get('reciepe_name')
        reciepe_description =  data.get('reciepe_description')
        
        print(reciepe_name)
        print(reciepe_description)
        print(reciepe_image)
        
        Reciepe.objects.create(
            reciepe_name = reciepe_name,
            reciepe_description = reciepe_description,
            reciepe_image = reciepe_image  
        )
        return redirect('/recipies/')
    queryset = Reciepe.objects.all()
    if request.GET.get('search'):
        queryset = queryset.filter(reciepe_image__icontains = request.GET.get('search'))
        
        
    context = {'reciepes':queryset}
    

    return render(request,'recipies.html' ,context)



def update_reciepe(request,id):
    queryset = Reciepe.objects.get(id=id)
    data = request.POST
    if request.method == 'POST':
        reciepe_image =  request.FILES.get('reciepe_image')
        reciepe_name =  data.get('reciepe_name')
        reciepe_description =  data.get('reciepe_description')
        
        queryset.reciepe_name = reciepe_name
        queryset.reciepe_description = reciepe_description
        
        if reciepe_image:
            queryset.reciepe_image = reciepe_image
        
        queryset.save()
        return redirect('/recipies/')
    
    context = {'reciepe': queryset}
    return render(request,'update_reciepe.html',context)



def delete_reciepe(request,id):
    queryset = Reciepe.objects.get(id=id)
    queryset.delete()
    return redirect('/recipies/')



def login_page(request):
        return render(request,'login.html')


def register_page(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')
               
        # Check if username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken. Please choose a different one.")
            return redirect('/register/')  # Redirect to the registration page again
        
        # Create user using create_user method
        user = User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username
        )
        user.set_password(password)
        user.save()
        messages.success(request, "Registration successful! Please log in.")
        return redirect('/register/')  # Redirect to the login page after successful registration

    return render(request, 'register.html')
