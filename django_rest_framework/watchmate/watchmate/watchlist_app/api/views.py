# Django
from django.shortcuts import get_object_or_404

# Django REST Framework
from rest_framework import generics, status, viewsets
from rest_framework.exceptions import ValidationError
from rest_framework.response  import Response
from rest_framework.views import APIView

# Local imports
from watchlist_app.models import Review, Watchlist, StreamPlatform
from watchlist_app.api.serializers import ReviewSerializer, StreamPlatformSerializer, WatchlistSerializer


# Class based view
# Watchlist
class WatchlistView(APIView):
    def get(self, request):
        watchlists = Watchlist.objects.all()
        serializer = WatchlistSerializer(watchlists, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = WatchlistSerializer(data=request.data, many=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class WatchlistDetailView(APIView):
    def get(self, request, pk):
        watchlist = get_object_or_404(Watchlist, pk=pk)
        serializer = WatchlistSerializer(watchlist)
        return Response(serializer.data)
    
    def put(self, request, pk):
        watchlist = get_object_or_404(Watchlist, pk=pk)
        serializer = WatchlistSerializer(watchlist, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def delete(self, request, pk):
        watchlist = get_object_or_404(Watchlist, pk=pk)
        watchlist.delete()
        return Response('Item deleted', status=status.HTTP_204_NO_CONTENT)

# Generics Views
class ReviewCreate(generics.CreateAPIView):
    serializer_class = ReviewSerializer
    
    def get_queryset(self):
        return Review.objects.all()
    
    def perform_create(self, serializer):
        watchlist = get_object_or_404(Watchlist, pk=self.kwargs['pk'])
        
        review_user = self.request.user
        review_queryset = Review.objects.filter(watchlist=watchlist, review_user=review_user)
        
        if review_queryset.exists():
            raise ValidationError('You have already reviewed this movie')
        
        serializer.save(watchlist=watchlist, review_user=review_user)
        
        

class ReviewList(generics.ListAPIView):
    # queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    
    def get_queryset(self):
        return Review.objects.filter(watchlist=self.kwargs['pk'])

class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class StreamPlatformVS(viewsets.ModelViewSet):
    queryset = StreamPlatform.objects.all()
    serializer_class = StreamPlatformSerializer