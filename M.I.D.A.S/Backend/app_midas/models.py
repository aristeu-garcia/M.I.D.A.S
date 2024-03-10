from django.db import models
from django.contrib.auth.models import User

class Group(models.Model):
    info = models.CharField(max_length=150, null=False, blank=False)
    
    def __str__(self) -> str:
        return self.info
    
    
class ClientGroup(models.Model):
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,  # Ajustado para CASCADE
        null=True,
        blank=False,
        related_name="client_groups"  # Renomeado para evitar conflitos
    )
    group = models.ForeignKey(
        to=Group,
        on_delete=models.CASCADE,  # Ajustado para CASCADE
        null=True,
        blank=False,
        related_name="client_groups"  # Renomeado para evitar conflitos
    )
    
    
class Commodity(models.Model):
    code = models.CharField(max_length=100, null=False, blank=False)
    name = models.CharField(max_length=100, null=False, blank=False)
    
    def __str__(self) -> str:
        return self.name
    
    
class Strategy(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    user = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name="strategies"  # Renomeado para evitar conflitos
    )
    commodity = models.ForeignKey(
        to=Commodity,
        on_delete=models.CASCADE,  # Ajustado para CASCADE
        null=False,
        blank=False,
        related_name="strategies"  # Renomeado para evitar conflitos
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
        related_name="sites"  # Renomeado para evitar conflitos
    )
    
    
class StrategySite(models.Model):
    strategy = models.ForeignKey(
        to=Strategy,
        on_delete=models.CASCADE,  # Ajustado para CASCADE
        null=True,
        blank=False,
        related_name="strategy_sites"  # Renomeado para evitar conflitos
    )
    site = models.ForeignKey(
        to=Site,
        on_delete=models.CASCADE,  # Ajustado para CASCADE
        null=True,
        blank=False,
        related_name="strategy_sites"  # Renomeado para evitar conflitos
    )
    
    
class Tokens(models.Model):
    token = models.CharField(max_length=100, null=False, blank=False)
    user = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name="tokens"  # Renomeado para evitar conflitos
    )
    
    
class StrategyToken(models.Model):
    strategy = models.ForeignKey(
        to=Strategy,
        on_delete=models.CASCADE,  # Ajustado para CASCADE
        null=True,
        blank=False,
        related_name="strategy_tokens"  # Renomeado para evitar conflitos
    )
    token = models.ForeignKey(
        to=Tokens,
        on_delete=models.CASCADE,  # Ajustado para CASCADE
        null=True,
        blank=False,
        related_name="strategy_tokens"  # Renomeado para evitar conflitos
    )
