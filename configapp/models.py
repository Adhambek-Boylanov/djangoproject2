from django.db import models

class Brand(models.Model):
    title = models.CharField(max_length=50)
    context = models.TextField()
    created_ed = models.DateTimeField(auto_now_add=True)
    upteaded_ed = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title

class AvtoSalon(models.Model):
    title = models.CharField(max_length=50)
    context = models.TextField(blank=True)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=50)
    addres = models.TextField(blank=True)
    image = models.ImageField(upload_to='photos/%Y/%m/%d')
    def __str__(self):
        return self.title
class Car(models.Model):
    model = models.CharField(max_length=50)
    price = models.IntegerField()
    yil = models.DateTimeField()
    colour = models.CharField(max_length=50)
    salon = models.ForeignKey(AvtoSalon,on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='photos/%Y/%m/%d')
    def __str__(self):
        return self.model



