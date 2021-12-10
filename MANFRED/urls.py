from    django.urls import  path
from    django.conf.urls.static import static
from    django.conf import  settings
from .import    views
urlpatterns = [
    path('',views.index,name='index'),
    path('xmas',views.xmas,name='xmas'),
    path('skills',views.skills,name='skills'),
]+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
