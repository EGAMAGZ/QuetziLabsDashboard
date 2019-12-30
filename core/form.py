from django import forms
from django.core import validators

class LoginForm(forms.Form):
    ad_email=forms.EmailField(label="email",widget=forms.EmailInput(attrs={'class':'form-control',
        'placeholder': 'Correo Electrónico'}),required=True,validators=[validators.validate_email,])
    ad_password=forms.CharField(label="password",widget=forms.PasswordInput(attrs={'class':'form-control',
        'placeholder':'Contraseña'}),required=True,min_length=6)
    ad_remember=forms.BooleanField(label="remember",widget=forms.CheckboxInput(attrs={'class':'form-check-input',}),required=False)

class RegisterForm(forms.Form):
    GENDER = (
        ("M","Hombre"),
        ("F","Mujer"),
    )
    ad_profile=forms.ImageField(label="profile image",validators=[validators.validate_image_file_extension,],required=False)
    ad_name=forms.CharField(label="name",max_length=60,min_length=15,required=True)
    ad_email=forms.EmailField(label="email",widget=forms.EmailInput(attrs={'class':'form-control','placeholder': 'Correo Electrónico'}),required=True,validators=[validators.validate_email,])
    ad_password=forms.CharField(label="password",widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Contraseña'}),required=True,min_length=6)
    ad_username=forms.CharField(min_length=6,max_length=30,required=True)
    ad_gender=forms.ChoiceField(choices=GENDER,required=True)
