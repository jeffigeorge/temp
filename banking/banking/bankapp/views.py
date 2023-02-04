from django.shortcuts import render, redirect, HttpResponseRedirect
from .models import Member
# Create your views here.

def index(request):
    if request.method == 'POST':
        member = Member(username=request.POST['username'], password=request.POST['password'])
        member.save()
        return render(request, 'login.html')
    else:
        return render(request, 'register.html')

def login(request):
    return render(request, 'login.html')

def home(request):

    if request.method == 'POST':
        if Member.objects.filter(username=request.POST['username'], password=request.POST['password']).exists():
            member = Member.objects.get(username=request.POST['username'], password=request.POST['password'])
            return render(request, 'home.html', {'member': member})

        else:
            context = {'msg': 'Invalid username or password'}
            return render(request, 'login.html', context)

def temp(request):
    if request.method == 'POST':
        context = {'msg': 'form registered'}
        return render(request, 'home.html', context)