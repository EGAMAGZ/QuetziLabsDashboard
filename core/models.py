from django.db import models

# Create your models here.
class QL_USR_DT(models.Model):
    GENDER = (
        ("M","Hombre"),
        ("F","Mujer"),
    )
    ql_usr_img_link=models.ImageField(upload_to="user-profile-picture")
    ql_usr_name=models.CharField(max_length=60)
    ql_usr_email=models.EmailField(unique=True)#By default the max_Length is 254
    ql_usr_pass=models.CharField(max_length=64)#hash256 max_length=64 bcrypt hash256 lenght=50
    ql_usr_username=models.CharField(max_length=30,unique=True)
    ql_usr_gender = models.CharField(max_length=1, choices=GENDER, default="M")

    ql_usr_created=models.DateTimeField(auto_now_add=True)

class QL_FREE_DT(models.Model):
    GENDER = (
        ("M","Hombre"),
        ("F","Mujer"),
    )
    ql_free_img_link=models.ImageField(upload_to="freelance-profile-picture")
    ql_free_name=models.CharField(max_length=60)
    ql_free_email=models.EmailField(max_length=254,unique=True)
    ql_free_pass=models.CharField(max_length=254)#hash256 max_length=64 bcrypt hash256 lenght=50
    ql_free_username=models.CharField(max_length=30,unique=True)
    ql_free_gender = models.CharField(max_length=1, choices=GENDER, default="M")

    ql_free_desc=models.TextField(max_length=500,blank=True)
    ql_free_created=models.DateTimeField(auto_now_add=True)