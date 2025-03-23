from rest_framework import serializers
from market_app.models import Market, Seller, Product


class MarketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Market
        fields = ["name", "location", "description", "net_worth"]
        # exclude = ["id"]

    def validate_name(self, value):
        errors = []

        if "x" in value:
            errors.append("There should be no x in value.")
        if "y" in value:
            errors.append("There should be no y in value.")

        if errors:
            raise serializers.ValidationError(errors)

        return value


class SellerSerializer(serializers.Serializer):
    class Meta:
        model = Seller
        fields = "__all__"


class SellerDeserializer(serializers.Serializer):
    class Meta:
        model: Seller
        fields = "__all__"


class ProductDeserializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
