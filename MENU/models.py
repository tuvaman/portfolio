
from django.db import models

# Create your models here.


class  Breakfast(models.Model):
    foods=models.CharField(max_length=200)
    class   Meta:
        verbose_name_plural='Breakfast'

    def __str__(self):
        return  self.foods
class  Lunch(models.Model):
    foods=models.CharField(max_length=200)
    class   Meta:
        verbose_name_plural='Lunch'

    def __str__(self):
        return  self.foods
class  Supper(models.Model):
    foods=models.CharField(max_length=200)
    class   Meta:
        verbose_name_plural='Supper'

    def __str__(self):
        return  self.foods


class  Days(models.Model):
    days_options=[('Monday','Monday'),
    ('Tuesday','Tuesday'),
    ('Wensday','Wensday'),
    ('Thursday','Thursday'),
    ('Friday','Friday'),
    ('Saturday','Saturday'),
    ('Sunday','Sunday'),]

    days=models.CharField(max_length=200,choices=days_options,null=True)
    def __str__(self):
        return  str(self.days).upper()
    class   Meta:
        verbose_name='Menu'
        verbose_name_plural='Menu'
        ordering=('id',)

class  Menu(models.Model):
    Day=models.ForeignKey(Days,on_delete=models.CASCADE,null=True)
    Breakfast=models.ManyToManyField(Breakfast,related_name='breakfast')
    Lunch=models.ManyToManyField(Lunch,related_name='lunch')
    Supper=models.ManyToManyField(Supper,related_name='supper')
    class   Meta:
        verbose_name_plural='Menu'
        ordering=('id',)

    def breakfast(self):
        return  "\n".join([str(b)  for b in self.Breakfast.all()])
        
    def lunch(self):
        return  "\n".join([str(l)  for l in self.Lunch.all()])
    def supper(self):
        return  "\n".join([str(s)  for s in self.Supper.all()])


    def __str__(self):
        return str(self.Day)