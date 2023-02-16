from django.db import models

# Create your models here.

def image_upload(instance, filename):
    imagename , extension = filename.split(".")
    return "contact/%s.%s"%(instance.id , extension)

class contact(models.Model): # table
    name= models.CharField(max_length=100); # reperesent a column
    office = models.CharField(max_length=100)
    email=models.EmailField(max_length=254)
    image = models.ImageField(upload_to=image_upload)

    def __str__(self):
        return self.name

