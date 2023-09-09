from django.shortcuts import render
from .models import *

# Create your views here.
def index_view(request):
    context = {
        'mashina' : Mashina.objects.all()
    }
    return render(request,'index.html',context)


def search_view(request):
    name = request.GET.get('name')
    cars = Mashina.objects.filter(name__icontains=name)
    context = {
        'cars':cars
    }
    return render(request,'search.html',context)


def car_detail_view(request,pk):
    car = Mashina.objects.get(id=pk)
    context ={
        "car":car
    }
    return render(request,'car-detail.html',context)

