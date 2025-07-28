from django.shortcuts import render, redirect
from .forms import *
from .models import *
def info(request):
    salon = AvtoSalon.objects.all()
    brand = Brand.objects.all()
    car = Car.objects.all()
    context = {
        "salon":salon,
        "brand":brand,
        "car":car
    }
    return render(request,'index.html',context=context)

def brand(request, pk, pk1):
    brand = Brand.objects.all()
    salon = AvtoSalon.objects.all()
    car = Car.objects.filter(brand_id = pk , salon_id =pk1)
    context = {
        "salon":salon,
        "brand":brand,
        "car":car
    }
    return render(request, 'brand.html',context=context)



def add_car(request):
    if request.method == "POST":
        form = CarForm(request.POST)
        if form.is_valid():
            car = Car.objects.create(**form.cleaned_data)
            return redirect('dashboard')
    else:
        form = CarForm()
    return render(request, 'add_car.html', {'form': form})


def add_brand(request):
    if request.method == "POST":
        form = BrandForm(request.POST)
        if form.is_valid():
            brand = Brand.objects.create(**form.cleaned_data)
    else:
        form = BrandForm()
    return render(request,'add_brand.html',context={'form':form})

def add_salon(request):
    if request.method == "POST":
        form = AvtosalonForm(request.POST)
        if form.is_valid():
            salon = AvtoSalon.objects.create(**form.cleaned_data)
    else:
        form = AvtosalonForm()
    return render(request,'add_salon.html',context={'form':form})












