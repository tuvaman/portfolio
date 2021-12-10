
from django.db import models

# Create your models here.

class Home(models.Model):
    name=models.CharField(max_length=200)
    greetings=models.CharField(max_length=200)
    picture=models.ImageField()
    logo=models.ImageField(null=True)
    updated=models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural='Home'

    def __str__(self):
        return  self.name
class About(models.Model):
    Title=models.CharField(max_length=200)
    Career=models.CharField(max_length=200)
    description=models.TextField()
    profile_picture=models.DateTimeField(auto_now=True)
    updated=models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name_plural='About'

    def __str__(self):
        return  self.Title


class Profile(models.Model):
    about=models.ForeignKey(About,on_delete=models.CASCADE,related_name='profile')
    social_name=models.CharField(max_length=100)
    link=models.URLField(max_length=200)
    
    class Meta:
        verbose_name_plural='Profile'



class  Category(models.Model):
    Title=models.CharField(max_length=200)
    updated=models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name='Topic'
        verbose_name_plural='Topics'

    def __str__(self):
        return  self.Title


class Skills(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    skill=models.CharField(max_length=100)
    
    class Meta:
        verbose_name_plural='Skills'
    

    def __str__(self):
        return  self.skill



class Portfolio(models.Model):
    image=models.ImageField()
    link=models.URLField(max_length=200)
    class   Meta:
        verbose_name_plural='Portfolio'
    def __str__(self):
        return  f'Portfolio{self.id}'