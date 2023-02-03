from distutils.command.upload import upload
from email.policy import default
from wsgiref.validate import validator
from django.db import models
from django.core.validators import MinValueValidator ,MaxValueValidator 
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Person(models.Model):

    genders = (
        ('M','Erkek'),
        ('F','Kadın'),
    )

    duty_types = (
        ('1','Görevli'),
        ('2','Oyuncu'),
        ('3','Yönetmen'),
        ('4','Senarist'),
    )

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    biography = models.CharField(max_length=3000)
    image = models.FileField(upload_to="images/cast",default="")
    date_of_birth = models.DateField()
    gender = models.CharField("cinsiyet",max_length=1, choices=genders)
    duty_type = models.CharField("görev",max_length=1, choices=duty_types)
    

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    full_name.fget.short_description = "ad-soyad"

    class Meta:
        verbose_name = "Kişi"
        verbose_name_plural = "Kişiler"

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.duty_types[int(self.duty_type)-1][1]})"
            

class Movie(models.Model):
    title = models.CharField("Başlık",max_length=100)
    description = RichTextField()
    image_name = models.FileField(upload_to="images/afisler",default="")
    image_cover = models.FileField(upload_to="images/covers",default="")
    date = models.DateField()
    slug = models.SlugField(unique=True,db_index=True)
    budget = models.DecimalField(max_digits=19,decimal_places=2)
    language = models.CharField(max_length=100)
    is_released = models.BooleanField(default=False)
    is_coming = models.BooleanField(default=True)
    people = models.ManyToManyField(Person)
    genres = models.ManyToManyField(Genre)
    rating = models.DecimalField(max_digits=2,decimal_places=1,null = True)
    

    class Meta:
        verbose_name = "Film"
        verbose_name_plural = "Filmler"

    def __str__(self):
        return self.title

class Comment(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    text = models.TextField(max_length=500)
    rating = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator (5)],default=1) #min ve max validatora gerek kalmadı aslında.çünkü bu alanı dropdown ile alıyoruz.input ile alsak evet gerek olabilirdi.ama ben silmedim örnek olarak dursun diye.
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE,related_name="comments")
    date_added = models.DateTimeField(null=True,auto_now=True)
    
    

class Video(models.Model):
    title = models.CharField(max_length=200)
    url = models.CharField(max_length=500)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return self.title