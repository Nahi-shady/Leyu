from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Parent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Parent')
    phone = models.CharField(max_length=100, verbose_name="Parent's Phone")
    address = models.CharField(max_length=100, verbose_name='Address')
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.user.username

class Child(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Child')
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE, related_name='children')
    disability = models.CharField(max_length=100, verbose_name='Disability')
    phone = models.CharField(max_length=100, verbose_name="Child's Phone")
    age = models.IntegerField(null=False, blank=False, verbose_name="Child's Age")
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Teacher')
    phone = models.CharField(max_length=100, verbose_name="Phone")
    address = models.CharField(max_length=100, verbose_name='Address')

    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username