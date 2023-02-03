
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm,PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from account.forms import LoginUserForm ,NewUserForm,UserForm,ProfileForm
from django.contrib.auth.decorators import login_required
from .models import Profile

def login_request(request):
    if request.user.is_authenticated:
        return redirect("home_page")

    if request.method == 'POST':
        form = LoginUserForm(request,data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            remember_me = form.cleaned_data.get("remember_me")
            user = authenticate(request=request,username=username,password=password)

            if user is not None:
                login(request,user)
                if not remember_me:
                    request.session.set_expiry(0)
                    request.session.modified=True
                    
                messages.success(request,"başarıyla giriş yapıldı")
                return redirect("home_page")
            else:
                return render(request,"account/login.html",{'form':form})
        else:
            return render(request,"account/login.html",{'form':form})  

    else:
        form = LoginUserForm()
        return render(request,"account/login.html",{'form':form})



    

def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save()
            """username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            user = authenticate(username=username,password=password)
            login(request=request,user=user)
            return redirect("home_page")"""

            messages.success(request,"yeni kayıt başarıyla oluşturuldu")
            return redirect("login")

        else:
            return render(request,"account/register.html",{"form":form})

    else:
        form = NewUserForm()
        return render(request,"account/register.html",{"form":form})

def change_password(request):
    if request.method =="POST":
        form = PasswordChangeForm(request.user,request.POST)

        if form.is_valid():
            user=form.save()
            update_session_auth_hash(request,user)
            messages.success(request,"parola başarılı bir şeklide değiştirildi")
            return redirect("change_password")
        else:
            return render(request,"account/change_password.html",{"form":form})
    else:
        form = PasswordChangeForm(request.user)
        return render(request,"account/change_password.html",{"form":form})


"""o kullanıcı için cookieyi siliyoruz"""
def logout_request(request):
    logout(request)
    messages.warning(request,"uygulamadan çıkıldı.")
    return redirect("home_page")


@login_required(login_url="/account/login")
def profile(request):
    if request.method == "POST":
        user_form=UserForm(request.POST,instance=request.user)
        profile_form = ProfileForm(request.POST,instance=request.user.profile,files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request,"profil bilgileri güncellendi.")
            return redirect("profile")
        else:
            messages.error(request,"lütfen bilgilerinizi konrtol ediniz")
    else:            
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)

    return render(request, 'account/profile.html',
    {"user_form":user_form,
    "profile_form":profile_form
    })


@login_required(login_url="/account/login")
def watch_list(request):
    user_id = request.user.id
    user = User.objects.get(id=user_id)
    watchList = user.profile.watch_list.all()
    return render(request, 'account/watch-list.html',{
        "watchList":watchList
    })