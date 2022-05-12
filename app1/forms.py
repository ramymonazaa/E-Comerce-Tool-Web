from asyncio.windows_events import NULL
from django import forms

from app1.models import tool

# class toolForm(forms.ModelForm):

#     class Meta:
#         model = tool
#         fields =['name','image','expiration_date','price', 'description','category']
#         widgets = {
#             'name': forms.TextInput(attrs={'class': 'form-control'}),
#             'image': forms.FileInput(attrs={'class': 'form-control'}),
#             'expiration_date': forms.TextInput(attrs={'class': 'form-control'}),
#             'price': forms.TextInput(attrs={'class': 'form-control'}),
#             'description': forms.TextInput(attrs={'class': 'form-control'}),
#             'category': forms.Select(attrs={'class': 'form-control'}),
#         }
