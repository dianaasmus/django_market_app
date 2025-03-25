from django.urls import path
from .views import (
    MarketView,
    MarketSingleView,
    SellersView,
    SellerSingleView,
    ProductView,
    ProductSingleView,
    MarketSellerView,
)

urlpatterns = [
    path("market/", MarketView.as_view()),
    path("market/<int:pk>/", MarketSingleView.as_view(), name="market-detail"),
    path("seller/", SellersView.as_view()),
    path("seller/<int:pk>/", SellerSingleView.as_view(), name="seller-detail"),
    path("product/", ProductView.as_view()),
    path("product/<int:pk>/", ProductSingleView.as_view(), name="product-detail"),
    path("market/<int:pk>/sellers/", MarketSellerView.as_view()),
]
