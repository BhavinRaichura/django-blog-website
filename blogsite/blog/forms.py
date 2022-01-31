

from django import forms
from blog.models import *

from django.core.exceptions import ValidationError


class NewClient(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Clients
        fields = ('username','email','phone_number','password')

    def clean_email(self):
        email = self.cleaned_data["email"]
        if Clients.objects.filter(email=email).exists():
            raise ValidationError("An user with this email already exists!")
        return email  
    
    def clean_username(self):
        username = self.cleaned_data["username"]
        if Clients.objects.filter(username=username).exists():
            raise ValidationError("An user with this user name already exists!")
        return username