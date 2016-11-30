from django.shortcuts import render, redirect
from .forms import Register_form, Login_form
from django.contrib.auth import authenticate, login, logout 

# Create your views here.

from django.http import HttpResponse
from sdp.models import Category, User, Course

def view_index(request, identity, username):    #need to handle HR and Administrator as well 
    this_user = User.objects.filter(username=username)
    if len(this_user)!=0:
        #return HttpResponse("OKay! " + username + " " + identity)
        category_list = (c.name for c in Category.objects.all())
        identity_list = this_user[0].get_identity_list()
        identity_list.remove(identity)
        Course.objects.
        arguments = {
        'category_list': category_list,
        'identity': identity,
        'identity_list': identity_list,
        'username': username}
        return render(request, 'index/view.html', arguments)
    else:
        return HttpResponse("Sorry! " + username + " " + identity)

def register(request):
    if request.method == 'POST':
        form = Register_form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Register success") #Redirect to index page 
        else:
            return HttpResponse("Error") #Invalid form (various reason)
    else:
        form = Register_form()
        return render(request, 'index/register.html', {'form':form})


def userlogin(request):
    if request.method == 'POST':
        form = Login_form(data=request.POST)
        if form.is_valid():
            user = authenticate(username=form['username'].data,password=form['password'].data)
            if user is not None:
                login(request,user)
                this_user = User.objects.filter(username=form['username'].data)
                identity = form['identity'].data
                category_list = (c.name for c in Category.objects.all())
                identity_list = this_user[0].get_identity_list()
                identity_list.remove(identity)
                arguments = {
                'category_list': category_list,
                'identity': identity,
                'identity_list': identity_list,
                'username': form['username'].data}
                print(form['username'].data + "Login!")
                #return render(request, 'index/view.html', arguments)
                return redirect('view_index', identity=identity,username=form['username'].data) #need to be completed 
            else:
                return HttpResponse("Error login message") #Return error login message 
        else:
            print(form.errors)
            print (form.non_field_errors)
            return HttpResponse("Invalid form")
    else:
        form = Login_form()
        return render(request, 'index/login.html', {'form':form})

def userlogout(request):
    logout(request)
    form = Login_form(data=request.POST)
    return redirect('login')



