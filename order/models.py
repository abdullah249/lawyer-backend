from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Orders(models.Model): 
  
    # fields of the model 
    title = models.CharField(max_length = 200) 
    description = models.TextField() 
    price=models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
  
    # renames the instances of the model 
    # with their title name 
    def __str__(self): 
        return self.title 