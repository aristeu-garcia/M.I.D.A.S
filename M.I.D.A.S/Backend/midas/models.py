from django.contrib.auth.models import AbstractUser
from django.db import models


class Client(AbstractUser):
    name = models.CharField(max_length=200, null=False, blank=False)
    email = models.EmailField(max_length=150, unique=True, null=True, blank=False)
    username = models.CharField(max_length=150, null=True, blank=False)
    cellphone = models.CharField(max_length=20, null=True, blank=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'cellphone']

    def __str__(self) -> str:
        return self.name


class Site(models.Model):
    site = models.CharField(max_length=200, null=False, blank=False)
    client = models.ForeignKey(to=Client, on_delete=models.CASCADE, null=True, blank=False,)
    
    def __str__(self) -> str:
        return self.site


class Token(models.Model):
    token = models.CharField(max_length=100, null=False, blank=False)
    client = models.ForeignKey(to=Client, on_delete=models.CASCADE, null=True, blank=False,)

    def __str__(self) -> str:
        return self.token


class Commodity(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    code = models.CharField(max_length=100, null=False, blank=False)
    client = models.ForeignKey(to=Client, on_delete=models.CASCADE, null=True, blank=False,)
    
    def __str__(self) -> str:
        return self.name


class Strategy(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    commodity = models.ForeignKey(to=Commodity, on_delete=models.CASCADE, null=True, blank=False)
    client = models.ForeignKey(to=Client, on_delete=models.CASCADE, null=True, blank=False)
    tokens = models.ManyToManyField(Token)
    sites = models.ManyToManyField(Site)
    
    def __str__(self) -> str:
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=150, null=True, blank=False)
    description = models.CharField(max_length=150, null=False, blank=False)
    admin = models.ForeignKey(to=Client, on_delete=models.CASCADE, null=True, blank=False, related_name='admin')
    participants = models.ManyToManyField(to=Client)
    
    def __str__(self) -> str:
        return self.info