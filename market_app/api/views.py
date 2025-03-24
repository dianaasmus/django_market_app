from rest_framework.views import APIView
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import (
    MarketSerializer,
    SellerSerializer,
    MarketHyperLinkedSerializer,
    ProductSerializer,
    ProductHyperLinkedSerializer,
)
from market_app.models import Market, Seller, Product


class MarketView(APIView):

    def get(self, request):
        markets = Market.objects.all()
        serializer = MarketHyperLinkedSerializer(
            markets, many=True, context={"request": request}
        )
        return Response(serializer.data)

    def post(self, request):
        serializer = MarketSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(["GET", "POST"])
# def market_view(request):

#     if request.method == "GET":
#         markets = Market.objects.all()
#         serializer = MarketHyperLinkedSerializer(
#             markets, many=True, context={"request": request}
#         )
#         return Response(serializer.data)

#     elif request.method == "POST":
#         serializer = MarketSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Single View
@api_view(["GET", "DELETE", "PUT"])
def market_single_view(request, pk):

    try:
        market = Market.objects.get(pk=pk)
    except Market.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = MarketHyperLinkedSerializer(market, context={"request": request})
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
        serializer = SellerSerializer(data=request.data)
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
        serializer = SellerSerializer(seller, context={"request": request})
        return Response(serializer.data)

    elif request.method == "DELETE":
        seller.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == "PUT":
        serializer = SellerSerializer(seller, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "POST"])
def product_view(request):

    if request.method == "GET":
        products = Product.objects.all()
        serializer = ProductHyperLinkedSerializer(
            products, many=True, context={"request": request}
        )
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def product_single_view(request, pk):

    try:
        products = Product.objects.get(pk=pk)
    except Seller.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = ProductHyperLinkedSerializer(
            products, context={"request": request}
        )
        return Response(serializer.data)

    elif request.method == "DELETE":
        products.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == "PUT":
        serializer = ProductSerializer(products, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
