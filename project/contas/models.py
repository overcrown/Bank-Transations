from django.db import models
from django.contrib.auth.models import User

# Create your models here.




class Category(models.Model):
    user = models.ForeignKey(User, related_name="category" ,on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)
    criation_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name



class Transation(models.Model):
    date = models.DateTimeField(auto_now=True)
    description = models.CharField(max_length = 200)
    value = models.DecimalField(max_digits=7, decimal_places = 2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    observation = models.TextField(null=True, blank=True)


    # Refeer to the internal caracteristcs of the class
    class Meta:
        verbose_name_plural = "Transations"

    # Return the name of itself, the description
    def __str__(self):
        return self.description
    


class Elements(models.Model):
    name = models.CharField(max_length=200)
    state = models.BooleanField()

    def __str__(self):
        return self.name and str(self.state)