from django.urls import path, include
from .views import (
    MarketView,
    MarketSingleView,
    SellersView,
    SellerSingleView,
    ProductView,
    ProductSingleView,
    MarketSellerView,
    ProductViewSet,
)
from rest_framework import routers

router = routers.SimpleRouter()
router.register(
    r"product",
    ProductViewSet,  # r = raw string (Ohne r könnten Backslashes (\) als Escape-Sequenzen interpretiert werden, wodurch der String möglicherweise ungewollt formatiert wird.)
)  # erzeugt automatisch mehrere URLs für ProductViewSet

urlpatterns = [
    path("", include(router.urls)),
    path("market/", MarketView.as_view()),
    path("market/<int:pk>/", MarketSingleView.as_view(), name="market-detail"),
    path("seller/", SellersView.as_view()),
    path("seller/<int:pk>/", SellerSingleView.as_view(), name="seller-detail"),
    path("product/", ProductView.as_view()),
    path("product/<int:pk>/", ProductSingleView.as_view(), name="product-detail"),
    path("market/<int:pk>/sellers/", MarketSellerView.as_view()),
]
