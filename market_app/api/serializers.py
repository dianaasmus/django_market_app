from rest_framework import serializers
from market_app.models import Market, Seller, Product


class MarketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Market
        fields = "__all__"

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
    # id = serializers.IntegerField(read_only=True)
    # name = serializers.CharField(max_length=225)
    # contact_info = serializers.CharField()
    # markets = MarketSerializer(many=True, read_only=True)
    # markets = serializers.StringRelatedField(many=True)
    class Meta:
        model = Seller
        fields = "__all__"


class SellerDeserializer(serializers.Serializer):
    # id = serializers.IntegerField(read_only=True)
    # name = serializers.CharField(max_length=225)
    # contact_info = serializers.CharField()
    # markets = serializers.ListField(child=serializers.IntegerField(), write_only=True)

    # def validate_markets(self, value):
    #     markets = Market.objects.filter(id__in=value)
    #     if len(markets) != len(value):
    #         raise serializers.ValidationError({"message": "Check nochmal die Ids"})
    #     return value

    # def create(self, validated_data):
    #     market_ids = validated_data.pop("markets")
    #     seller = Seller.objects.create(**validated_data)
    #     markets = Market.objects.filter(id__in=market_ids)
    #     seller.markets.set(markets)
    #     return seller

    # def update(self, instance, validated_data):
    #     market_ids = validated_data.pop("markets")
    #     instance.id = validated_data.get("id", instance.id)
    #     instance.name = validated_data.get("name", instance.name)
    #     instance.contact_info = validated_data.get(
    #         "contact_info", instance.contact_info
    #     )
    #     markets = Market.objects.filter(id__in=market_ids)
    #     instance.markets.set(markets)
    #     instance.save()
    #     return instance
    class Meta:
        model: Seller
        fields = "__all__"


class ProductDeserializer(serializers.ModelSerializer):
    # id = serializers.IntegerField(read_only=True)
    # name = serializers.CharField(max_length=225)
    # description = serializers.CharField()
    # price = serializers.DecimalField(max_digits=100, decimal_places=2)
    # markets = serializers.IntegerField()
    # sellers = serializers.IntegerField()

    # def create(self, validated_data):
    #     market_id = validated_data.pop("markets")
    #     seller_id = validated_data.pop("sellers")

    #     market = Market.objects.get(id=market_id)
    #     seller = Seller.objects.get(id=seller_id)

    #     new_product = Product(
    #         name=validated_data["name"],
    #         description=validated_data["description"],
    #         price=validated_data["price"],
    #         markets=Market.objects.get(id=market_id),
    #         sellers=Seller.objects.get(id=seller_id),
    #     )

    #     # product = Product.objects.create(**validated_data)

    #     # ManyToMany-Felder setzen
    #     # product.markets.set(market)
    #     # product.sellers.set(seller)
    #     return new_product
    class Meta:
        model = Product
        fields = "__all__"
