from    django.urls import  path
from    django.conf.urls.static import static
from    django.conf import  settings
from .import    views
urlpatterns = [
    path('',views.index,name='index'),
    path('xmas',views.xmas,name='xmas'),
    path('skills',views.skills,name='skills'),
]

if  settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
