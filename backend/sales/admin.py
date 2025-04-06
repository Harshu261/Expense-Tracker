from django.contrib import admin
from .models import RawItem,MainItem,PlateSale
# Register your models here.
admin.site.register(MainItem)
admin.site.register(RawItem)
admin.site.register(PlateSale)
