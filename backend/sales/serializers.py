from rest_framework import serializers
from .models import PlateSale,RawItem,MainItem


class MainItemSerializer(serializers.ModelSerializer) :
    class Meta :
        model = MainItem
        fields = '__all__'
class PlateSaleSerializer(serializers.ModelSerializer):
    main_item = MainItemSerializer(read_only=True)
    date = serializers.DateField()
    main_item_id = serializers.PrimaryKeyRelatedField(
        queryset=MainItem.objects.all(),
        source='main_item',
        write_only=True
    )

    class Meta:
        model = PlateSale
        fields = ['id', 'main_item', 'main_item_id', 'quantity', 'price_per_plate', 'date']
class RawItemSerializer(serializers.ModelSerializer) :
    class Meta :
        model = RawItem
        fields = '__all__'
