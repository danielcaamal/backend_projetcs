# Django

# Django REST Framework
from rest_framework import serializers

# Local imports
from watchlist_app.models import Watchlist, StreamPlatform, Review


# # Basic serializer, one to one relationship
# # Function validators
# def _validate_name(self, value):
#     if len(value) < 2:
#         raise serializers.ValidationError("Name must be at least 2 characters long")
#     return value

# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(max_length=50, validators=[_validate_name])
#     description = serializers.CharField(max_length=200)
#     active = serializers.BooleanField(default=True)
    
#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance
    
#     # Field level validation
#     def validate_name(self, value):
#         if len(value) < 2:
#             raise serializers.ValidationError("Name must be at least 2 characters long")
#         return value
    
#     # Object level validation
#     def validate(self, data):
#         if data['name'] == 'test':
#             raise serializers.ValidationError("Name cannot be 'test'")
#         return data

# Review Serializer
class ReviewSerializer(serializers.ModelSerializer):
    review_user = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = Review
        exclude = ('watchlist',)


# Model Serializer
class WatchlistSerializer(serializers.ModelSerializer):
    # len_name = serializers.SerializerMethodField()
    reviews = ReviewSerializer(many=True, read_only=True)
    # reviews = serializers.ReadOnlyField(source="reviews.rating")
    
    class Meta:
        model = Watchlist
        fields = "__all__"
        # exclude = ('active',)
    
    # def get_len_name(self, obj):
    #     return len(obj.name)

class StreamPlatformSerializer(serializers.ModelSerializer):
    # watchlist = WatchlistSerializer(many=True, read_only=True)
    watchlist = serializers.StringRelatedField(many=True, read_only=True) # For showing watchlist names
    # watchlist = serializers.PrimaryKeyRelatedField(many=True, read_only=True) # For showing watchlist ids
    # watchlist = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='watchlist-details')
    
    class Meta:
        model = StreamPlatform
        fields = "__all__"