from rest_framework import serializers
from market_app.models import Market, Seller, Product


class MarketSerializer(serializers.ModelSerializer):
    sellers = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Market
        exclude = []

    def validate_name(self, value):
        errors = []

        if "x" in value:
            errors.append("There should be no x in value.")
        if "y" in value:
            errors.append("There should be no y in value.")

        if errors:
            raise serializers.ValidationError(errors)

        return value


class MarketHyperLinkedSerializer(
    MarketSerializer, serializers.HyperlinkedModelSerializer
):

    class Meta:
        model = Market
        exclude = []


class SellerSerializer(serializers.ModelSerializer):
    markets = MarketSerializer(many=True, read_only=True)
    market_ids = serializers.PrimaryKeyRelatedField(
        queryset=Market.objects.all(), many=True, write_only=True, source="markets"
    )

    market_count = serializers.SerializerMethodField()

    class Meta:
        model = Seller
        fields = ["id", "name", "contact_info", "market_count", "markets", "market_ids"]

    def get_market_count(self, obj):
        return obj.markets.count()


class SellerDeserializer(serializers.ModelSerializer):
    class Meta:
        model: Seller
        fields = "__all__"


class ProductDeserializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
