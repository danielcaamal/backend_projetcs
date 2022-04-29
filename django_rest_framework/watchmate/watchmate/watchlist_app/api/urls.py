# Django
from django.urls import path, include

# Django REST Framework
from rest_framework.routers import DefaultRouter
# Local imports
# from watchlist_app.api.views import movie_list, movie_details
from watchlist_app.api.views import ReviewCreate, ReviewDetail, ReviewList, StreamPlatformVS, WatchlistView, WatchlistDetailView



router = DefaultRouter()

router.register('stream', StreamPlatformVS, basename='streamplatform')

urlpatterns = [
    # Function based view
    # path('list/', movie_list, name='movie-list'),
    # path('<int:pk>', movie_details, name='movie-details'),
    # Class based view
    path('watch/', WatchlistView.as_view(), name='watchlist'),
    path('watch/<int:pk>', WatchlistDetailView.as_view(), name='watchlist-details'),
    # path('stream/', StreamPlatformView.as_view(), name='stream'),
    # path('stream/<int:pk>', WatchlistDetailView.as_view(), name='stream-details'),
    path('', include(router.urls)),
    path('watch/review/<int:pk>', ReviewDetail.as_view(), name='review-details'),
    path('watch/<int:pk>/review/', ReviewList.as_view(), name='review'),
    path('watch/<int:pk>/review-create/', ReviewCreate.as_view(), name='review-create'),
    
    
    # path('watch/<int:pk>/review/<int:pk>', WatchlistDetailView.as_view(), name='stream-details'),
    
    
    # path('review/', ReviewList.as_view(), name='review'),
    # path('review/<int:pk>', ReviewDetail.as_view(), name='review-details'),
    
    
]