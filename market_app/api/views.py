from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import (
    MarketSerializer,
    SellerSerializer,
    SellerDeserializer,
    ProductDeserializer,
)
from market_app.models import Market, Seller, Product


@api_view(["GET", "POST"])
def market_view(request):

    if request.method == "GET":
        markets = Market.objects.all()
        serializer = MarketSerializer(markets, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = MarketSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Single View
@api_view(["GET", "DELETE", "PUT"])
def market_single_view(request, pk):

    try:
        market = Market.objects.get(pk=pk)
    except Market.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = MarketSerializer(market)
        return Response(serializer.data)

    elif request.method == "DELETE":
        market.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == "PUT":
        serializer = MarketSerializer(market, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data, status=status.HTTP_200_OK
            )  #!!! sonst bei error status 200
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "POST"])
def seller_view(request):

    if request.method == "GET":
        sellers = Seller.objects.all()
        serializer = SellerSerializer(sellers, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = SellerDeserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "DELETE", "PUT"])
def seller_single_view(request, pk):

    try:
        seller = Seller.objects.get(pk=pk)
    except Seller.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = SellerSerializer(seller)
        return Response(serializer.data)

    elif request.method == "DELETE":
        seller.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == "PUT":
        serializer = SellerDeserializer(seller, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "POST"])
def product_view(request):

    if request.method == "GET":
        products = Product.objects.all()
        serializer = ProductDeserializer(products, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = ProductDeserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
