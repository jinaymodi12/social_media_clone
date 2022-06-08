from django.shortcuts import render
from .forms import *
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import *
from django.db.models import Q 
from django.core.paginator import Paginator

# Create your views here.

@login_required(login_url='/login/')
def home(request):
    uid = AddPost.objects.all()[::-1]
    p = Paginator(AddPost.objects.all(),4)
    page = request.GET.get('page')
    c = p.get_page(page)
    return render(request,'index.html',{'uid':uid,'c':c})

def logins(request):
    form1=LoginForm()
    if request.method == 'POST':
        form=LoginForm(request=request,data=request.POST)
        if form.is_valid():
            user=authenticate(request,username=form.cleaned_data['username'],password=form.cleaned_data['password'])
            print(user)
            if user is not None:         
                login(request,user)
                return redirect('index')  
            else:
               return redirect('sigin')  
        else:
            print(form.errors)
            messages.info(request,'Enter correct username')
            return redirect('sigin')    
    return render(request,'login.html',{'form':form1})

def signupp(request):
    form1=SignUp()
    if request.method == 'POST':
        form=SignUp(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'Create Profile Successfully!')
            return redirect('sigin')
        else:
            print(form.errors)
            messages.error(request,'Error!')
            return redirect('signup')
    else:
        return render(request,'signup.html',{'form':form1})
    
def logoutt(request):
    logout(request)
    return redirect('sigin')

@login_required(login_url='/login/')
def add_post(request):
    form1=AddPostForm()
    if request.method == 'POST':
        form=AddPostForm(request.POST,request.FILES)
        if form.is_valid():
            f=form.save(commit=False)
            f.user=request.user
            f.save()
            messages.success(request,'Add Post Successfully!')
            return redirect('index')
        else:
            print(form.errors)
            messages.error(request,'Error!')
            return redirect('add-post')
    return render(request,'add-post.html',{'form':form1})

@login_required(login_url='/login/')
def profiles(request):
    uid = AddPost.objects.filter(user=request.user)[::-1]
    tid = User.objects.filter(follower=request.user)
    return render(request,'profile.html',{'uid':uid,'tid':tid})

@login_required(login_url='/login/')
def profile_edit(request):
    form1=EditForm(instance=request.user)
    if request.method == 'POST':
        form=EditForm(request.POST,request.FILES,instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
        else:
            messages.error(request,'ERROR!!')
            return redirect('profile')
    return render(request,'edit.html',{'form':form1})

@login_required(login_url='/login/')
def likes(request,pk):
    uid = AddPost.objects.get(id=pk)
    uid.like.add(request.user)
    uid.save()
    return redirect('index')

@login_required(login_url='/login/')
def dislikes(request,pk):
    uid = AddPost.objects.get(id=pk)
    uid.like.remove(request.user)
    uid.save()
    return redirect('index')

@login_required(login_url='/login/')
def view_profiles(request,pk):
    uid = User.objects.get(id=pk)
    all = AddPost.objects.filter(user=uid)
    al = AddPost.objects.filter(post=request.user)
    return render(request,'view-profile.html',{'uid':uid,'all':all,'al':al})

@login_required(login_url='/login/')
def following(request,pk):
    uid = User.objects.filter(id=pk).last()  
    uid.followers.add(request.user)
    uid.save()
    request.user.following.add(uid)
    request.user.save()
    return redirect('view-profile',pk)

@login_required(login_url='/login/')
def un_follow(request,pk):
    uid = User.objects.filter(id=pk).last() 
    uid.followers.remove(request.user)
    uid.save()
    request.user.following.remove(uid)
    request.user.save()
    return  redirect('view-profile',pk)

@login_required(login_url='/login/')
def followings(request,pk):
    uid = User.objects.filter(id=pk).last()  
    uid.save()
    return render(request,'view-profile.html',{'uid':uid})

@login_required(login_url='/login/')
def searched(request):
    searc = request.GET['search']
    if searc <= '0':
        return redirect('index')
    else:
        names = User.objects.filter(name__icontains=searc)
        posts = AddPost.objects.filter(post=request.user)
    return render(request,'search.html',{'searc':searc,'names':names,'posts':posts})

@login_required(login_url='/login/')
def post_detail(request,pk):
    uid = AddPost.objects.get(id=pk)
    tid = Comment.objects.filter(add_post=uid)[::-1]
    form1=CommentForm()
    if request.method == 'POST':
        form=CommentForm(request.POST)
        if form.is_valid():
            f=form.save(commit=False)
            f.user=request.user
            f.add_post=uid
            f.save()
            return render(request,'post-detail.html',{'uid':uid,'tid':tid,'form':form1})
        else:
            print(form.errors)
            messages.error(request,'Error!')
            return redirect('post-detail')
    else:
        return render(request,'post-detail.html',{'uid':uid,'tid':tid,'form':form1})


@login_required(login_url='/login/')
def view_friend(request):
    return render(request,'view-friend.html')
    