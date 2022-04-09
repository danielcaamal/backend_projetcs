from django.urls import path, include

urlpatterns = [
    path('', include('snippets.urls')),
]

# Authentication
urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]