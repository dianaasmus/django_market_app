from .serializers import (
    ProductHyperLinkedSerializer,
    SellerSerializer,
    MarketHyperLinkedSerializer,
    ProductSerializer,
)
from market_app.models import Market, Seller, Product
from rest_framework import generics


class MarketView(generics.ListCreateAPIView, generics.DestroyAPIView):
    queryset = Market.objects.all()
    serializer_class = MarketHyperLinkedSerializer


class MarketSingleView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Market.objects.all()
    serializer_class = MarketHyperLinkedSerializer


class SellersView(generics.ListAPIView, generics.CreateAPIView):
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer


class SellerSingleView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer


class ProductView(generics.ListCreateAPIView):
    queryset = Product.objects.all()

    def get_serializer_class(self):
        if self.request.method == "POST":
            return ProductSerializer
        return ProductHyperLinkedSerializer


class ProductSingleView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductHyperLinkedSerializer

    def get_serializer_class(self):
        if self.request.method == "GET":
            return ProductHyperLinkedSerializer
        return ProductSerializer
