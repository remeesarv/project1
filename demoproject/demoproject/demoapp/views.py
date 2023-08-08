from django.shortcuts import render
from . models import Place
from . models import Members
# Create your views here.
def demo(request):
    obj=Place.objects.all
    obj2 = Members.objects.all
    return render(request,"index.html",{'result':obj,'res':obj2})

