from django.db import models
from django.template.context_processors import request


class CarModel(models.Model):
    title = models.CharField(max_length=50)
    brithdate = models.IntegerField()
    created_ed = models.DateTimeField(auto_now_add=True)
    update_ed = models.DateTimeField(auto_now=True)


class Cars(models.Model):
    title = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    horsepower = models.IntegerField()
    year = models.IntegerField()
    price = models.IntegerField()
    model = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    context = models.TextField(blank=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    created_ed = models.DateTimeField(auto_now_add=True)
    update_ed = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "CAR"
        verbose_name_plural = "CARS"
        ordering = ['-created_ed']
