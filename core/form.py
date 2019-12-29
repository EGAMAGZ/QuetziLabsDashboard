from django import forms
from django.core import validators

class LoginForm(forms.Form):
    ad_email=forms.EmailField(label="email",widget=forms.EmailInput(attrs={'class':'form-control','placeholder': 'Correo Electrónico'}),required=True,validators=[validators.validate_email,])
    ad_password=forms.CharField(label="password",widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Contraseña'}),required=True,min_length=6)
    ad_remember=forms.BooleanField(label="remember",widget=forms.CheckboxInput(attrs={'class':'form-check-input',}),required=False)

class RegisterForm(forms.Form):
    ad_email=forms.EmailField(label="email",widget=forms.EmailInput(attrs={'class':'form-control','placeholder': 'Correo Electrónico'}),required=True,validators=[validators.validate_email,])
    ad_password=forms.CharField(label="password",widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Contraseña'}),required=True,min_length=6)
