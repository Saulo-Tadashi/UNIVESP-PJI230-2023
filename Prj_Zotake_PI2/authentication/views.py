from django.shortcuts import render
from django.contrib.auth.models import User

def signin (request):
    if request.method == 'GET':
        return render(request, 'signin.html')
    name = request.POST.get('nome')
    username = request.POST.get('usuario')
    password = request.POST.get('senha')

    user = User.object.filter(username=username).first()



def login (request):
    if request.method=='GET':
        return render(request, 'login.html')
    username = request.POST.get('usuario')
    password = request.POST.get('senha')
