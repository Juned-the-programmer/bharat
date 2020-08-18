from django.db import models

# Create your models here.
class product(models.Model):
    name = models.CharField(max_length=500)
    description = models.CharField(max_length=1000)
    company_name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    price = models.IntegerField()
    image = models.ImageField(null=True,blank=True)
    

    def __str__(self):
        return self.name
    