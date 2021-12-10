from django.shortcuts import render
from .models  import    Home,About,Profile, Skills,Category

# Create your views here.

def index(request):
    home=Home.objects.get(id=1)
    about=About.objects.get(id=1)
    facebook=Profile.objects.get(social_name='Facebook')
    sololearn=Profile.objects.get(social_name='sololearn')
    return  render(request,'index.html',{'home':home,'about':about,'facebook':facebook,'sololearn':sololearn})



def xmas(request):
    return  render(request,'inndex.html')




def skills(request):
    title=Category.objects.all()
    
    web=Skills.objects.get(id=1)

    return  render(request,'skills.html',{'skills':web,'title':title})



