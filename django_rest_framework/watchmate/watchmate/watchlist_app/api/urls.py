# Django
from django.urls import path, include

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Local imports
from watchlist_app.api.views import ReviewCreate, ReviewDetail, ReviewList, StreamPlatformVS, WatchlistView, WatchlistDetailView

router = DefaultRouter()

router.register('stream', StreamPlatformVS, basename='streamplatform')

urlpatterns = [
    # Watch routes
    path('watch/', WatchlistView.as_view(), name='watchlist'),
    path('watch/<int:pk>', WatchlistDetailView.as_view(), name='watchlist-details'),
    path('watch/review/<int:pk>', ReviewDetail.as_view(), name='review-details'),
    path('watch/<int:pk>/review/', ReviewList.as_view(), name='review'),
    path('watch/<int:pk>/review-create/', ReviewCreate.as_view(), name='review-create'),
    
    # Stream Routes
    path('', include(router.urls)),
]