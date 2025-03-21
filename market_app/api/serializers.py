from rest_framework import serializers
from market_app.models import Market, Seller


def validate_no_x(value):
    errors = []

    if "x" in value:
        errors.append("There should be no x in value.")
    if "y" in value:
        errors.append("There should be no y in value.")

    if errors:
        raise serializers.ValidationError(errors)

    return value


class MarketSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=225)
    location = serializers.CharField(max_length=225, validators=[validate_no_x])
    description = serializers.CharField()
    net_worth = serializers.DecimalField(max_digits=100, decimal_places=2)

    def create(self, validated_data):
        return Market.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.id = validated_data.get("id", instance.id)
        instance.name = validated_data.get("name", instance.name)
        instance.location = validated_data.get("location", instance.location)
        instance.description = validated_data.get("description", instance.description)
        instance.net_worth = validated_data.get("net_worth", instance.net_worth)
        instance.save()
        return instance

    def validate_location(self, value):
        if "x" in value:
            raise serializers.ValidationError("There should be no x in location")
        return value


class SellerSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=225)
    contact_info = serializers.CharField()
    markets = MarketSerializer(many=True, read_only=True)
    # markets = serializers.StringRelatedField(many=True)


class SellerDeserializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=225)
    contact_info = serializers.CharField()
    markets = serializers.ListField(child=serializers.IntegerField(), write_only=True)

    def validate_markets(self, value):
        markets = Market.objects.filter(id__in=value)
        if len(markets) != len(value):
            raise serializers.ValidationError({"message": "Check nochmal die Ids"})
        return value

    def create(self, validated_data):
        market_ids = validated_data.pop("markets")
        seller = Seller.objects.create(**validated_data)
        markets = Market.objects.filter(id__in=market_ids)
        seller.markets.set(markets)
        return seller

    def update(self, instance, validated_data):
        market_ids = validated_data.pop("markets")
        instance.id = validated_data.get("id", instance.id)
        instance.name = validated_data.get("name", instance.name)
        instance.contact_info = validated_data.get(
            "contact_info", instance.contact_info
        )
        markets = Market.objects.filter(id__in=market_ids)
        instance.markets.set(markets)
        instance.save()
        return instance
