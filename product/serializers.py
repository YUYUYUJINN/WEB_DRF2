from rest_framework import serializers
from product.models import Product
from review.serializers import ReviewSerializer


class ProductSerializer(serializers.ModelSerializer):
    review_set = ReviewSerializer(many=True, read_only=True)
    review_set_count = serializers.IntegerField(source='review_set.count', read_only=True)
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'review_set', 'review_set_count']
