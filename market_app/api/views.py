from rest_framework.views import APIView
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import (
    MarketSerializer,
    SellerSerializer,
    MarketHyperLinkedSerializer,
    ProductSerializer,
)
from market_app.models import Market, Seller, Product
from rest_framework import mixins, generics
from django.http import Http404

from market_app.api import serializers


class MarketView(
    mixins.ListModelMixin,  # Ermöglicht das Abrufen einer Liste von Market-Objekten (GET)
    mixins.CreateModelMixin,  # Ermöglicht das Erstellen neuer Market-Objekte (POST)
    generics.GenericAPIView,  # Stellt Grundfunktionen für DRF-Views bereit, wie queryset, serializer_class, get_serializer(), etc.
):
    queryset = Market.objects.all()
    serializer_class = MarketHyperLinkedSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class MarketSingleView(
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    mixins.UpdateModelMixin,
    generics.GenericAPIView,
):
    serializer_class = MarketSerializer

    def get_object(self, pk):
        try:
            return Market.objects.get(pk=pk)
        except Market.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        market = self.get_object(pk)
        serializer = MarketHyperLinkedSerializer(market, context={"request": request})
        return Response(serializer.data)

    def delete(self, pk):
        market = self.get_object(pk)
        market.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk):
        market = self.get_object(pk)
        serializer = MarketSerializer(market, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SellersView(
    mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView
):
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class SellerSingleView(
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    mixins.UpdateModelMixin,
    generics.GenericAPIView,
):
    serializer_class = SellerSerializer

    def get_object(self, pk):
        try:
            return Seller.objects.get(pk=pk)
        except Seller.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        seller = self.get_object(pk)
        serializer = SellerSerializer(seller, context={"request": request})
        return Response(serializer.data)

    def delete(self, pk):
        seller = self.get_object(pk)
        seller.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk):
        seller = self.get_object(pk)
        serializer = SellerSerializer(seller, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductView(
    mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView
):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


# @api_view(["GET", "PUT", "DELETE"])
# def product_single_view(request, pk):

#     try:
#         products = Product.objects.get(pk=pk)
#     except Seller.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == "GET":
#         serializer = ProductSerializer(products, context={"request": request})
#         return Response(serializer.data)

#     elif request.method == "DELETE":
#         products.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

#     elif request.method == "PUT":
#         serializer = ProductSerializer(products, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductSingleView(
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    mixins.UpdateModelMixin,
    generics.GenericAPIView,
):
    serializer_class = ProductSerializer

    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        product = self.get_object(pk)
        serializer = ProductSerializer(product, context={"request": request})
        return Response(serializer.data)

    def delete(self, pk):
        product = self.get_object(pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk):
        product = self.get_object(pk)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
