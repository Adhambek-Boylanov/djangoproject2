from django import forms
from .models import *

class CarForm(forms.Form):
    model = forms.CharField(label="Madelnomi", max_length=100, widget=forms.TextInput(attrs={"class": "form-control"}))
    price = forms.IntegerField(label="Narxi",  widget=forms.NumberInput(attrs={"class": "form-control"}))
    yil = forms.DateField(label="yili")
    colour = forms.CharField(label="rangi",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
    salon = forms.ModelChoiceField(empty_label="Avtosalon",
                                      label="categories",queryset=AvtoSalon.objects.all(),
                                      widget=forms.Select(attrs={"class":"form-control"}))
    brand = forms.ModelChoiceField(empty_label="Brand",
                                      label="categories",queryset=Brand.objects.all(),
                                      widget=forms.Select(attrs={"class":"form-control"}))
class BrandForm(forms.Form):
    title = forms.CharField(label="brand",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
    context = forms.CharField(label="context",required=False ,widget=forms.Textarea(attrs={"class":"form-control"}))

class AvtosalonForm(forms.Form):
    title = forms.CharField(label="Avtosalon", max_length=50, widget=forms.TextInput(attrs={"class": "form-control"}))
    context = forms.CharField(label="context", required=False, widget=forms.Textarea(attrs={"class": "form-control"}))
    eamil = forms.CharField(label="email", max_length=100, widget=forms.TextInput(attrs={"class": "form-control"}))
    phone = forms.CharField(label="phone", max_length=50, widget=forms.TextInput(attrs={"class": "form-control"}))
    addres = forms.CharField(label="addres", required=False, widget=forms.Textarea(attrs={"class": "form-control"}))
