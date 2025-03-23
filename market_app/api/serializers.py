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
        fields = ["id", "url", "name", "location", "description", "net_worth"]


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
