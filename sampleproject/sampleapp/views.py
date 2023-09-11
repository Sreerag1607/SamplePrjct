from django.shortcuts import render
from django.http import HttpResponse

from . models import Place, Team


# Create your views here.
def demo(request):
    obj=Place.objects.all()
    team=Team.objects.all()
    return render(request,"index.html",{'result':obj,'tem':team})

# def add(request):
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     res=x+y
#     return render(request,"abt.html",{'addition':res})
#
# def contact(request):
#     return HttpResponse("this is contact page")