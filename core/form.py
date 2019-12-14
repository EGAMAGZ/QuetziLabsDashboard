from django import forms
from django.core import validators

class LoginForm(forms.Form):
    ad_email=forms.EmailField(label="email",widget=forms.EmailInput(attrs={'class':'form-control',}),required=True,validators=[validators.validate_email,])
    ad_password=forms.CharField(label="password",widget=forms.PasswordInput(attrs={'class':'form-control',}),required=True,min_length=6)