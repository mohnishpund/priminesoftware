from rest_framework import serializers

from .models import Booking
from django import forms


from django.contrib.auth.models import User 


class BookingSerializer(serializers.ModelSerializer):
     class Meta:
        model = Booking
        fields = '__all__'
        
        
class DataSerializer(forms.ModelForm):
     class Meta:
        model = Booking
        #fields = '__all__'
        fields = ('Name', 'author', 'Address', 'Phone_number', 'Khasara', 'Advisoryname')
        widgets = {
		           'Name': forms.TextInput(attrs={'class': 'form-control'}),
                 'author': forms.Select(attrs={'class': 'form-control'}),
		           'Address': forms.TextInput(attrs={'class': 'form-control'}),
		           'Phone_number.': forms.TextInput(attrs={'class': 'form-control'}),
		           'Khasara': forms.TextInput(attrs={'class': 'form-control'}),
		           'Advisoryname': forms.TextInput(attrs={'class': 'form-control'}),

                 }