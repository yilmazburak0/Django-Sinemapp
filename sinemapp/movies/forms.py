from django import forms
from django.forms import widgets

from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        numbers = {
            ("1","1 yıldız"),
            ("2","2 yıldız"),
            ("3","3 yıldız"),
            ("4","4 yıldız"),
            ("5","5 yıldız"),
        }
        model = Comment
        #fields = ["full_name","email"]
        exclude = ['movie','date_added',]
        labels = {"full_name":"Ad Soyad","text":"Yorum"}

        widgets= {
            "full_name":widgets.TextInput(attrs={"class":"form-control"}),
            "email":widgets.EmailInput(attrs={"class":"form-control"}),
            "text":widgets.Textarea(attrs={"class":"form-control"}),
            "rating":widgets.Select(attrs={"class":"form-control custom-select"},choices=numbers),
        }
