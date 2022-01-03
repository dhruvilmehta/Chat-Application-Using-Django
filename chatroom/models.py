from django.db import models

# Create your models here.
class Host(models.Model):
    hostname=models.CharField(max_length=10)
    meetcode=models.IntegerField(unique=True)

class chatdata(models.Model):
    name=models.CharField(max_length=10)
    message=models.CharField(max_length=100)
    relatehost=models.ForeignKey(Host,on_delete=models.CASCADE)