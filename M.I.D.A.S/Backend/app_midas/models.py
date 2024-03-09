from django.db import models
from django.contrib.auth.models import User


class Group(models.Model):
    info = models.CharField(max_length=150, null=False, blank=False)
    
    def __str__(self) -> str:
        return self.info
    
    
class ClientGroup(models.Model):
    user = models.ForeignKey(
        to=User,
        null=True,
        blank=False,
        related_name="user"
    )
    group = models.ForeignKey(
        to=Group,
        null=True,
        blank=False,
        related_name="group"
    )
    
    
class Commodity(models.Model):
    code = models.CharField(max_length=100, null=False, blank=False)
    name = models.CharField(max_length=100, null=False, blank=False)
    
    def __str__(self) -> str:
        return self.name
    
    
class Strategy(models.Model):
    name = models.CharField(max_lenght=100, null=False, blank=False)
    user = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name="user"
    )
    commodity = models.ForeignKey(
        to=Commodity,
        null=False,
        blank=False,
        related_name="user"
    )
    
    def __str__(self) -> str:
        return self.name
    
    
class Site(models.Model):
    url = models.CharField(max_length=200, null=False, blank=False)
    user = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name="user"
    )
    
    
class StrategySite(models.Model):
    strategy = models.ForeignKey(
        to=Strategy,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name="strategy"
    )
    site = models.ForeignKey(
        to=Site,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name="user"
    )
    
    
class Tokens(models.Model):
    token = models.CharField(max_length=100, null=False, blank=False)
    user = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name="user"
    )
    
    
class StrategyToken(models.Model):
    strategy = models.ForeignKey(
        to=Strategy,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name="strategy"
    )
    token = models.ForeignKey(
        to=Tokens,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name="user"
    )