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
    path('list/', WatchlistView.as_view(), name='watchlist'),
    path('<int:pk>/', WatchlistDetailView.as_view(), name='watchlist-details'),
    path('review/<int:pk>/', ReviewDetail.as_view(), name='review-details'),
    path('<int:pk>/reviews/', ReviewList.as_view(), name='review'),
    path('<int:pk>/review-create/', ReviewCreate.as_view(), name='review-create'),
    
    # Stream Routes
    path('', include(router.urls)),
]