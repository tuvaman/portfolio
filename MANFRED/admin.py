from django.contrib import admin
from django.db import models

# Register your models here.
from .models    import  Home,About,Profile,Category,Skills,Portfolio

class   ProfileAdmin(admin.TabularInline):
    model=Profile
    extra=1
class  SkillsAdmin(admin.TabularInline):
    model=Skills
    extra=2
@admin.register(About)
class  AboutAdmin(admin.ModelAdmin):
    inlines=[ProfileAdmin,]

@admin.register(Category)
class  CategoryAdmin(admin.ModelAdmin):
    inlines=[SkillsAdmin,]
    list_per_page=1



admin.site.register(Home)
admin.site.register(Portfolio)
