from django.db import models

# Create your models here.
class QL_USR_DT(models.Model):
    ql_usr_img_link=models.ImageField(upload_to="user-profile-picture")
    ql_usr_name=models.CharField(max_length=60)
    ql_usr_email=models.EmailField()#By default the max_Length is 254
    ql_usr_username=models.CharField(max_length=30)

class QL_FREE_DT(models.Model):
    ql_usr_img_link=models.ImageField(upload_to="freelance-profile-picture")
    ql_free_name=models.CharField(max_length=60)
    ql_free_email=models.EmailField(max_length=254)
    ql_free_desc=models.TextField(max_length=500)