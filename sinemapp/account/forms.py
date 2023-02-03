from dataclasses import field, fields
from pyexpat.errors import messages
from django import forms
from django.forms import widgets
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib import messages
from django.contrib.auth.models import User

from account.models import Profile

class LoginUserForm(AuthenticationForm):
    remember_me = forms.BooleanField(required=False, initial=False, widget=forms.CheckboxInput(attrs={"class":"custom-control-input"}))
    
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields["username"].widget = widgets.TextInput(attrs={"class":"form-control"})
        self.fields["password"].widget = widgets.PasswordInput(attrs={"class":"form-control"})

    def clean_username(self):
        username = self.cleaned_data.get("username")

        if username == "admin":
            messages.success(self.request,"hoş geldin admin")
        return username  

    def confirm_login_allowed(self, user):
        if user.username.startswith("q"):
            return forms.ValidationError("bu kullanıcı adıyla login olamazsınız")

class NewUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = {"username","email","first_name","last_name"}

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields["password1"].widget = widgets.PasswordInput(attrs={"class":"form-control"})
        self.fields["password2"].widget = widgets.PasswordInput(attrs={"class":"form-control"})
        self.fields["username"].widget = widgets.TextInput(attrs={"class":"form-control"})
        self.fields["first_name"].widget = widgets.TextInput(attrs={"class":"form-control"})
        self.fields["last_name"].widget = widgets.TextInput(attrs={"class":"form-control"})
        self.fields["email"].widget = widgets.EmailInput(attrs={"class":"form-control"})
        self.fields["email"].required = True
        self.fields["first_name"].required = True
        self.fields["last_name"].required = True

    def clean_email(self):
        email = self.cleaned_data.get("email") 

        if User.objects.filter(email=email).exists():
            self.add_error("email","email daha önce kullanılmış.")
        return email 

    #username için UserCreationForm kontrol yapıyor.       

    def clean_first_name(self):
        first_name = self.cleaned_data.get("first_name") 

        if " " in first_name:
            self.add_error("first_name","isim boşluk karekteri içeremez")

        if any(char.isdigit() for char in first_name):
            self.add_error("first_name","isim sayı içeremez")

        if any(not c.isalnum() for c in first_name):
            self.add_error("first_name","isim özel karekter içeremez")    

        return first_name    

    def clean_last_name(self):
        last_name = self.cleaned_data.get("last_name") 

        if " " in last_name:
            self.add_error("last_name","soyad boşluk karekteri içeremez")

        if any(char.isdigit() for char in last_name):
            self.add_error("last_name","soyad sayı içeremez")      

        if any(not c.isalnum() for c in last_name):
            self.add_error("last_name","soyad özel karekter içeremez")

        return last_name         


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("first_name","last_name","email",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["first_name"].widget = widgets.TextInput(attrs={"class":"form-control","placeholder":"First Name"})
        self.fields["last_name"].widget = widgets.TextInput(attrs={"class":"form-control","placeholder":"Last Name"})
        self.fields["email"].widget = widgets.EmailInput(attrs={"class":"form-control","placeholder":"Email"})

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ("avatar","location",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["location"].widget = widgets.TextInput(attrs={"class":"form-control","placeholder":"Location"})   