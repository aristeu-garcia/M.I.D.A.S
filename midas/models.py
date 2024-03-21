from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(max_length=150, null=False, blank=False, unique=True)
    password = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self) -> str:
        return self.name


class Group(models.Model):
    info = models.CharField(max_length=150, null=False, blank=False)
    
    def __str__(self) -> str:
        return self.info
    
    
class ClientGroup(models.Model):
    user = models.ForeignKey(
        to=Client,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name="user"
    )
    group = models.ForeignKey(
        to=Group,
        on_delete=models.SET_NULL,
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
    name = models.CharField(max_length=100, null=False, blank=False)
    user = models.ForeignKey(
        to=Client,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name="strategy_user"
    )
    commodity = models.ForeignKey(
        to=Commodity,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name="user_commodity"
    )
    
    def __str__(self) -> str:
        return self.name
    
    
class Site(models.Model):
    url = models.CharField(max_length=200, null=False, blank=False)
    user = models.ForeignKey(
        to=Client,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name="user_site"
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
        related_name="site_strategy"
    )
    
    
class Tokens(models.Model):
    token = models.CharField(max_length=100, null=False, blank=False)
    user = models.ForeignKey(
        to=Client,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name="user_token"
    )
    
    
class StrategyToken(models.Model):
    strategy = models.ForeignKey(
        to=Strategy,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name="strategy_token"
    )
    token = models.ForeignKey(
        to=Tokens,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name="tokens"
    )