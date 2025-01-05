from django.db import models

class User(models.Model):
    id = models.AutoField(primary_key=True)  
    name = models.CharField(max_length=150)  
    email = models.EmailField(unique=True)  
    username = models.CharField(max_length=150, unique=True) 
    password = models.CharField(max_length=128)  

    def __str__(self):
        return self.username

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')  
    title = models.CharField(max_length=200)
    content = models.TextField() 
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)  

    def __str__(self):
        return self.title
