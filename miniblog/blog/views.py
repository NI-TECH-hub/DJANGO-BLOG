

from audioop import add
from .models import Post
# from pyexpat.errors import messages
from django.shortcuts import render,HttpResponseRedirect
from django.contrib import messages
from .forms import PostForm, SignUpForm,LogInForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import Group

# Create your views here.

#Home
def Home(request):
    posts = Post.objects.all()
    return render(request,'blog/Home.html',{'posts':posts})

#About
def About(request):
    return render(request,'blog/About.html')

#Contact
def Contact(request):
    return render(request,'blog/contact.html')

#Dashboard
def Dashboard(request):
    if request.user.is_authenticated:
        posts = Post.objects.all()
        user = request.user
        full_name = user.get_full_name()
        grp = user.groups.all()
        return render(request,'blog/dashboard.html',{'posts':posts,'full_name':full_name,'groups':grp})
    else:
        return HttpResponseRedirect('/login')


#login
def user_sign_in(request):
    # if user is not login
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = LogInForm(request=request,data = request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username=uname,password=upass)
                if user is not None:
                    login(request,user)
                    messages.success(request,'Logged in Successfully !!')
                    return HttpResponseRedirect('/dashboard')
        else:
            form = LogInForm()
        return render(request,'blog/signIN.html',{'form':form})
    else:
        return HttpResponseRedirect('/dashboard')

#signup
def user_sign_up(request):

    if request.method == "POST":
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            messages.success(request,'Congratulations!! You Have Become an Author.')
            fm.save()
          
    else:

     fm = SignUpForm()
    return render(request,'blog/signUP.html',{'form':fm})


#Logout
def user_log_out(request):
    logout(request)
    return HttpResponseRedirect('/')

#Add New Post
def add_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/dashboard/')
    else:
        form = PostForm()
    return render(request,'blog/addpost.html',{'form':form})
    
#Update Post
def update_post(request,id):
    if request.user.is_authenticated:
        if id:
            data = Post.objects.get(id = id)
            if request.method == "POST":
                form = PostForm(data=request.POST,instance=data)
                if form.is_valid():
                    form.save()
                    return HttpResponseRedirect('/dashboard')
            else:
                
                form = PostForm(instance=data)              
            return render(request,'blog/updatepost.html',{'form':form})
        return HttpResponseRedirect('/dashboard')
    else:
        return HttpResponseRedirect('/login')

#delete Post
def delete_post(request,id):
    if request.user.is_authenticated:
        if id:
            data = Post.objects.get(pk = id)
            data.delete()
        return HttpResponseRedirect('/dashboard')
    else:
        return HttpResponseRedirect('/login')