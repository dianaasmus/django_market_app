from rest_framework import serializers
from market_app.models import Market, Seller, Product


class SellerSerializer(serializers.ModelSerializer):
    markets = serializers.HyperlinkedRelatedField(
        many=True, view_name="market-detail", read_only=True
    )
    market_ids = serializers.PrimaryKeyRelatedField(
        queryset=Market.objects.all(), many=True, write_only=True, source="markets"
    )

    market_count = serializers.SerializerMethodField()

    class Meta:
        model = Seller
        fields = ["id", "name", "contact_info", "market_count", "markets", "market_ids"]

    def get_market_count(self, obj):
        return obj.markets.count()


class SellerListSerializer(SellerSerializer, serializers.ModelSerializer):
    class Meta:
        model = Seller
        fields = ["name", "contact_info", "market_count", "markets", "market_ids"]


class MarketSerializer(serializers.ModelSerializer):
    sellers = SellerSerializer(many=True, read_only=True)

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


class MarketHyperLinkedSerializer(MarketSerializer, serializers.ModelSerializer):
    # sellers = serializers.(read_only=True)

    def __init__(self, *args, **kwargs):
        # Don't pass the 'fields' arg up to the superclass
        fields = kwargs.pop("fields", None)

        # Instantiate the superclass normally
        super().__init__(*args, **kwargs)

        if fields is not None:
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)

    class Meta:
        model = Market
        fields = [
            "id",
            "name",
            "location",
            "sellers",
            "description",
            "net_worth",
        ]


class ProductHyperLinkedSerializer(serializers.ModelSerializer):
    market = serializers.HyperlinkedRelatedField(
        view_name="market-detail", read_only=True
    )
    seller = serializers.HyperlinkedRelatedField(
        view_name="seller-detail", read_only=True
    )

    class Meta:
        model = Product
        fields = ["id", "name", "description", "price", "market", "seller"]


class ProductSerializer(serializers.ModelSerializer):
    market = serializers.PrimaryKeyRelatedField(queryset=Market.objects.all())
    seller = serializers.PrimaryKeyRelatedField(queryset=Seller.objects.all())

    class Meta:
        model = Product
        fields = ["id", "name", "description", "price", "market", "seller"]
