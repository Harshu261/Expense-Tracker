from django.db import models
from django.utils import timezone
# Create your models here.
class RawItem(models.Model) :
    name = models.CharField(max_length = 100)
    cost_price = models.DecimalField(max_digits = 10, decimal_places = 2)
    date = models.DateField(default=timezone.now)
    def __str__(self) :
        return self.name
    def get_cost_price(self) :
        return self.cost_price

class MainItem(models.Model) :
    name = models.CharField(max_length = 100)
    cost_price = models.DecimalField(max_digits = 10, decimal_places = 2)
    components =  models.ManyToManyField(RawItem,blank=True,related_name="main_items")
    def __str__(self) :
        return self.name
    def get_cost_price(self) :
        return self.cost_price
    def get_price_per_plate(self) :
        return self.price_per_plate
class PlateSale(models.Model) :
    main_item = models.ForeignKey(MainItem,default = None, on_delete=models.CASCADE,related_name="plate_sales")
    date = models.DateField(default=timezone.now)
    quantity = models.PositiveIntegerField(default = 1)
    price_per_plate = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self) :
        return f"{self.quantity} plate(s) sold on {self.date}"
    def total_sold(self) :
        return self.price_per_plate * self.quantity
