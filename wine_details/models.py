from django.db import models

# Create your models here.


class wine_details(models.Model):
    country = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    designation = models.TextField(blank=True, null=True)
    points = models.DecimalField(max_digits=5, decimal_places=0)
    price = models.IntegerField(null=True)
    province = models.CharField(max_length=150, blank=True)
    region_1 = models.CharField(max_length=150, blank=True)
    region_2 = models.CharField(max_length=150, blank=True)
    variety = models.CharField(max_length=150, blank=True)
    winery = models.CharField(max_length=150)

    def __str__(self):
        return self.winery
