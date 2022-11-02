from pyexpat import model
from django import forms

class contactForm(forms.Form):
 name= forms.CharField(max_length=100)
 email= forms.EmailField()
 content=forms.CharField(widget=forms.Textarea)