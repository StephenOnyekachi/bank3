import random

from django.shortcuts import render

from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import Users

def user_logout(request):
    logout(request)
    return redirect('home')

def user_login(request):
    if request.method == 'POST':
        username = request.POST['name']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_superuser:
                login(request, user)
                return redirect('index')
            else:
                login(request, user)
                return redirect('dashbord')
        else:
            messages.info(request, 'username or password is incorrect')
            return redirect('admin_login')
    context = {
        'message': messages,
    }
    return render(request, 'login.html', context)

def home(request):
    context = {
        # 'comment': comment,
    }
    return render(request, 'home.html', context)

def index(request):
    context = {
        # 'comment': comment,
    }
    return render(request, 'index.html', context)

def user(request):
    user = Users.objects.filter(is_superuser=False).order_by('-id')
    context = {
        'user': user,
    }
    return render(request, 'widgets.html', context)

def user_edit(request, pk):
    user = Users.objects.get(id=pk)
    if request.method == 'POST':
        # username = request.POST['name']
        # email = request.POST['email']
        # number = request.POST['number']
        # address = request.POST['address']
        # gender = request.POST['gender']
        balance = request.POST['balance']
        # type = request.POST['type']

        # user.username = username
        user.balance = balance
        # user.email = email
        # user.number = number
        # user.address = address
        # user.gender = gender
        # user.type = type
        user.save()
        return redirect('user')
    context = {
        'user': user,
    }
    return render(request, 'edit.html', context)

def user_delete(request, pk):
    user = Users.objects.get(id=pk)
    if request.method == 'POST':
        user.delete()
        return redirect('user')
    context = {
        'user': user,
    }
    return render(request, 'delete.html', context)

def user_block(request, pk):
    user = Users.objects.get(id=pk)
    if request.method == 'POST':

        if user.block:
            user.block = False
            user.save()
            return redirect('user')

        user.block = True
        user.save()
        return redirect('user')
    context = {
        'user': user,
    }
    return render(request, 'block.html', context)

def new_user(request):
    uni = '001'
    rand1 = str(random.randint(10000000, 99999999))
    ticket = uni + rand1
    # ticket = int(ticket)
    while len(Users.objects.filter(account=ticket)) != 0:
        rand1 = str(random.randint(1000, 9999))
        ticket = uni + rand1
        ticket = int(ticket)
    if request.method == 'POST':
        username = request.POST['name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        number = request.POST['number']
        address = request.POST['address']
        gender = request.POST['gender']
        type = request.POST['type']
        account = ticket

        if password1 == password2:
            if Users.objects.filter(username=username).exists():
                messages.info(request, 'Username taken')
                return redirect('new_user')
            elif Users.objects.filter(email=email).exists():
                messages.info(request, 'email taken')
                return redirect('new_user')
            else:
                user = Users.objects.create_user(username=username, email=email, password=password1,
                    type=type, account=account, number=number, gender=gender, address=address)
                user.save()
                messages.success(request, 'account was created successfully')
                return redirect('user')
        else:
            messages.info(request, 'password not matching...')
            return redirect('new_user')
    context = {
        'message': messages,
    }
    # return render(request, 'new_user.html', context)
    return render(request, 'form-wizard.html', context)

def charts(request):
    context = {
        # 'comment': comment,
    }
    return render(request, 'charts.html', context)

def dashbord(request):
    user = Users.objects.get(username=request.user)
    context = {
        'user': user,
    }
    return render(request, 'Dashboard.html', context)

def profile(request):
    user = Users.objects.get(username=request.user)
    context = {
        'user': user,
    }
    return render(request, 'profile.html', context)

def profile_settings(request):
    user = Users.objects.get(username=request.user)
    if request.method == 'POST':
        fund1 = request.POST['pin1']
        fund2 = request.POST['pin2']
        if fund2 == fund1:
            fund = Users.objects.create_user(fund=fund1)
    context = {
        'user': user,
        # 'fund': fund,
    }
    return render(request, 'profile_settings.html', context)

def transfer(request):
    user = Users.objects.get(username=request.user)
    context = {
        'user': user,
    }
    return render(request, 'Fund_Transfer.html', context)

def info(request):
    context = {}
    if request.method == 'GET':
        sender = Users.objects.get(username=request.user)
        search = request.GET.get('account')
        receiver = Users.objects.get(account=search)
        amount = request.GET['amount']

        context = {
            'receiver': receiver,
            'sender': sender,
            'amount': amount,
        }
    return render(request, 'info.html', context)


def send_funds(request):
    if request.method == 'POST':
        search = request.POST.get('search')
        print(search)
        amount = request.POST['amount']
        receiver = Users.objects.get(account=search)
        sender = request.user
        if sender.balance < int(amount):
            messages.info(request, 'insufficient balance try again')
            return redirect('transfer')
        else:
            receiver.balance += int(amount)
            receiver.save()
            sender.balance -= int(amount)
            sender.save()
            messages.info(request, 'success')
            return redirect('dashbord')
    

# def funds(request):
#     # receiver = Users.objects.get(id=pk)
#     if request.method == 'GET':
#         search = request.GET.get('account')
#         user = Users.objects.all().filter(account=search)
#     context = {
#         'user': user,
#     }
#     return render(request, 'transfer.html', context)



