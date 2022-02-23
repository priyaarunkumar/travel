from django.db import models

# Create your models here.
class place(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to ='priya')
    desc=models.TextField()

    # def __str__(self):
    #     return self.name;
class cricket(models.Model):
    na=models.CharField(max_length=250)
    im=models.ImageField(upload_to='pic')
    des=models.TextField()



