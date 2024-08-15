from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    peoples=[
        {'name':"prashant",'age': 23},
        {'name':"pankaj",'age': 24},
        {'name':"aditya",'age': 19},
        {'name':"harshdip",'age': 19},
        {'name':"shilwan",'age': 25},
        ]
    text = '''this is slicing in django ellendus nihil commodi ipsum quia veritatis vero, sint rem temporibus impedit provident, soluta quisquam fuga.</p>'''
    vegitable = ['pumpkine','tomato','potato',]
    return render(request, "index.html",context={'peoples':peoples,'text':text, 'vegitables': vegitable, "page": "Django 2024 "})

def about(request):
    context = {'page':"About"}
    return render(request,"about.html", context)

def contact(request):
    context = {'page' : "contact"}
    return render(request,"contact.html", context)