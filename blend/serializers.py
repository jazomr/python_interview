from rest_framework import serializers
from blend.models import StockSearch


class StockSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = StockSearch
        fields = ["symbol", "price"]
