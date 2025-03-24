from django.urls import path
from .views import (
    market_view,
    market_single_view,
    seller_view,
    seller_single_view,
    product_view,
    product_single_view,
)

urlpatterns = [
    path("market/", market_view),
    path("market/<int:pk>/", market_single_view, name="market-detail"),
    path("seller/", seller_view),
    path("seller/<int:pk>/", seller_single_view, name="seller_single_view"),
    path("product/", product_view),
    path("product/<int:pk>/", product_single_view, name="product-detail"),
]
