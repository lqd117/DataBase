from django.http import HttpResponse
from django.shortcuts import render
from .models import User
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.template import RequestContext

def index(request):
    return render(request, 'research/index.html', {})

@login_required(login_url='/login/do_login')
def home(request):
    return render(request,
                  'research/home.html',
                  {'username': request.user.username})

def do_login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    db_info = User.objects.filter(user_name=username)
    if db_info.__len__()==0:
        return render(request,'research/index.html',{'password_is_wrong':True})
    elif db_info[0].user_password == password:
        return redirect(reverse('research:home'))
    else:
        return render(request, 'research/index.html', {'password_is_wrong': True})


