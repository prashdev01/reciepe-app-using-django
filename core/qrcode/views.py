from django.shortcuts import render,redirect
from django.http import HttpResponse

def qr_gen(request):
    return render(request,'qr_code.html')
    