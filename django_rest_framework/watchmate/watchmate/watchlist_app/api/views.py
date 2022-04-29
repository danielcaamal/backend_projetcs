# Django
from django.shortcuts import get_object_or_404

# Django REST Framework
from rest_framework import generics, mixins, status, viewsets
# from rest_framework.decorators import api_view
from rest_framework.exceptions import ValidationError
from rest_framework.response  import Response
from rest_framework.views import APIView

# Local imports
from watchlist_app.models import Review, Watchlist, StreamPlatform
from watchlist_app.api.serializers import ReviewSerializer, StreamPlatformSerializer, WatchlistSerializer


# Function based view
# # API endpoint to list all movies
# @api_view(['GET', 'POST'])
# def movie_list(request):
#     if request.method == 'GET':
#         movies = Movie.objects.all()
#         serializer = WatchlistSerializer(movies, many=True)
#         return Response(serializer.data)
    
#     elif request.method == 'POST':
#         serializer = WatchlistSerializer(data=request.data, many=True)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)
        

# # API endpoint for a single movie
# @api_view(['GET', 'POST', 'PUT', 'DELETE'])
# def movie_details(request, pk):
#     if request.method == 'GET':
#         movie = get_object_or_404(Movie, pk=pk)
#         serializer = WatchlistSerializer(movie)
#         return Response(serializer.data)
    
#     elif request.method == 'PUT':
#         movie = get_object_or_404(Movie, pk=pk)
#         serializer = WatchlistSerializer(movie, data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)
    
#     elif request.method == 'DELETE':
#         movie = get_object_or_404(Movie, pk=pk)
#         movie.delete()
#         return Response('Item deleted', status=status.HTTP_204_NO_CONTENT)


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


# StreamPlatform views

# class StreamPlatformView(APIView):
#     def get(self, request):
#         platform = StreamPlatform.objects.all()
#         serializer = StreamPlatformSerializer(platform, many=True, context={'request': request})
#         return Response(serializer.data)
    
#     def post(self, request):
#         serializer = StreamPlatformSerializer(data=request.data, many=True)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)
    
# class StreamPlatformDetailView(APIView):
#     def get(self, request, pk):
#         stream_platform = get_object_or_404(StreamPlatform, pk=pk)
#         serializer = StreamPlatformSerializer(stream_platform)
#         return Response(serializer.data)
    
#     def put(self, request, pk):
#         stream_platform = get_object_or_404(StreamPlatform, pk=pk)
#         serializer = StreamPlatformSerializer(stream_platform, data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)
    
#     def delete(self, request, pk):
#         stream_platform = get_object_or_404(StreamPlatform, pk=pk)
#         stream_platform.delete()
#         return Response('Item deleted', status=status.HTTP_204_NO_CONTENT)

# Mixin based views
# class ReviewList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer
    
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

# class ReviewDetail(mixins.RetrieveModelMixin, generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer
    
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

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


# Viewsets and Routers
# class StreamPlatformVR(viewsets.ViewSet):
#     def list(self, request):
#         queryset = StreamPlatform.objects.all()
#         serializer = StreamPlatformSerializer(queryset, many=True)
#         return Response(serializer.data)
    
#     def retrieve(self, request, pk=None):
#         queryset = StreamPlatform.objects.all()
#         stream = get_object_or_404(queryset, pk=pk)
#         serializer = StreamPlatformSerializer(stream)
#         return Response(serializer.data)

#     def create(self, request):
#         stream_platform = get_object_or_404(StreamPlatform, pk=pk)
#         serializer = StreamPlatformSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)

class StreamPlatformVS(viewsets.ModelViewSet):
    queryset = StreamPlatform.objects.all()
    serializer_class = StreamPlatformSerializer