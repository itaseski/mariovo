from django.db import models


# Ограноци, врски и патишта кои поврзуваат се нарекуваат цдBranch, link and connecting roads, called Class-B roads, have three-digit numbers above 130.
class LocalRoud(models.Model):
    edge = models.CharField(max_length=5)  # L80522
    steam = models.CharField(max_length=4)  # R1107
    distance = models.IntegerField()
