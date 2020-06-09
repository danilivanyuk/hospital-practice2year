from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate, login, logout
from django.forms import inlineformset_factory

from .models import *
from .forms import *

def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name='doctor')
            user.groups.add(group)

            Doctor.objects.create(
			user=user,
			name=user.username,
			)

            messages.success(request, 'Account was created for '+username)
            return redirect('login')

    context = {'form':form}
    return render(request, 'Doctors/register.html', context)

def loginPage(request):
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or password is incorrect')

    context ={}
    return render(request, 'Doctors/login.html', context)

def logOut(request):
    logout(request)
    return redirect('login')

def home(request):
    doctor_id = request.user.id
    clients = request.user.doctor.client_set.all()
    context = {'clients':clients, 'doctor_id':doctor_id}
    
    return render(request, 'Doctors/user.html', context)

def addClient(request, pk):
    pk = request.user.doctor.id
    print(pk)
    doctor = Doctor.objects.get(id=pk)
    ClientFormSet = inlineformset_factory(Doctor, Client, fields=('name','phone',
    'cost','category','additionalInfo','analys_pic', 'next_visit'))
    formset = ClientFormSet()

    if request.method == 'POST':
        formset = ClientFormSet(request.POST, instance=doctor)
        if formset.is_valid():
            formset.save()
            return redirect('/')

    context = {'formset':formset}
    
    return render(request, 'Doctors/client_form.html', context)

def deleteClient(request, pk):
    client = Client.objects.get(id=pk)

    if request.method == 'POST':
        client.delete()
        return redirect('/')
        
    context = {'client':client}
    return render(request, 'Doctors/delete.html', context)