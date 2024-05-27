# from django.shortcuts import render
import json
from rest_framework import permissions, viewsets
from blend.models import StockSearch
from blend.serializers import StockSerializer
from blend.business.alphavantage_stock import AlphavantageStockModel
from blend.business.polygon_stock import PolygonStockModel
from blend.models import StockSearch
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action
from rest_framework.response import Response


# Create your views here.
class StockSearchViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = StockSearch.objects.all()
    serializer_class = StockSerializer
    # permission_classes = [permissions.IsAuthenticated]

    @action(detail=False, methods=["get"])
    def get_stock(self, request, pk=None):
        symbol = request.GET.get("symbol")
        # user_id = Token.objects.get(key=request.auth.key).user_id
        user_id = 1
        try:
            business = AlphavantageStockModel()
            price = business.get_current_price(symbol)
        except Exception:
            try:
                business = PolygonStockModel()
                price = business.get_current_price(symbol)
            except Exception:
                return Response("Symbol not Found")

        StockSearch.objects.create(user_id=user_id, symbol=symbol, price=price)

        return Response(dict(symbol=symbol, price=price))
