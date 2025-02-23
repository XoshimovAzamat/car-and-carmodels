from django.urls import path, include
from .views import *

urlpatterns = [
    path('index/', index),
    path('carmodels/<int:model_id>', carmodels, name='carmodels'),
    path('details/<int:car_id>', details, name='details'),

]
