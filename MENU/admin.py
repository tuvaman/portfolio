from django.contrib import admin
from  .models   import  Breakfast,Lunch,Supper,Menu,Days


admin.site.register(Breakfast)
admin.site.register(Lunch)
admin.site.register(Supper)

class   MenuAdmin(admin.TabularInline):
    model=Menu
    list_display=['Day','breakfast','lunch','supper']
    extra=0

@admin.register(Days)
class  DaysAdmin(admin.ModelAdmin):
    inlines=[MenuAdmin,]
    # Register your models here.
