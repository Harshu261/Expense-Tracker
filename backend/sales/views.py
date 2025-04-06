from rest_framework import viewsets
from .models import PlateSale,RawItem,MainItem
from .serializers import PlateSaleSerializer,RawItemSerializer,MainItemSerializer

class PlateSaleViewSet(viewsets.ModelViewSet) :
    queryset = PlateSale.objects.all()
    serializer_class = PlateSaleSerializer
class RawItemViewSet(viewsets.ModelViewSet) :
    queryset = RawItem.objects.all()
    serializer_class = RawItemSerializer
class MainItemViewSet(viewsets.ModelViewSet) :
    queryset = MainItem.objects.all()
    serializer_class = MainItemSerializer
