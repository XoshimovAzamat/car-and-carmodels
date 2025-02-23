from django.shortcuts import render
from .models import *

def index(request):
    carmodel = CarModel.objects.all()
    cars = Cars.objects.all()
    context = {
        "carmodel":carmodel,
        "cars":cars,
        "title":"Car Models"
    }
    return render(request, 'index.html', context=context)

def carmodels(request, model_id):
    carmodels = CarModel.objects.all()
    cars = Cars.objects.filter(model_id=model_id)
    context = {
        "carmodels":carmodels,
        "cars":cars,
        'title':"Car Models",
    }
    return render(request, 'carmodels.html', context=context)

def details(request, car_id):
    cars = Cars.objects.get(pk=car_id)
    context = {
        'car': cars
    }
    return render(request, 'details.html', context=context)