from django.db import models

# Create your models here.
class QL_USR_DT(models.Model):
    ql_usr_img_link=models.ImageField(upload_to="user-profile-picture")
    ql_usr_name=models.CharField(max_length=60)
    ql_usr_email=models.EmailField(max_length=254)
    ql_usr_username=models.CharField(max_length=30)