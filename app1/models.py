from django.db import models

# Create your models here.
class category(models.Model):
    name = models.CharField(max_length=200)
    discription=models.CharField(max_length=200)
    def __str__(self):
        return self.name
    
class tool(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    image= models.ImageField()
    expiration_date = models.FloatField()
    price=models.FloatField()
    category=models.ForeignKey(category,related_name="category",on_delete=models.CASCADE,default=True,null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
    
class serves(models.Model):
    name=models.CharField(max_length=100)
    numberOfTools=models.IntegerField()
    tool=models.ForeignKey(tool, related_name="employees",on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    
    
    
    
    #models.py File

# from django.db import models


# class Post(models.Model):
#     title= models.CharField(max_length=300, unique=True)
#     content= models.TextField()