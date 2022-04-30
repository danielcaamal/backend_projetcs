# Django
from django.urls import path

# Django REST Framework
from rest_framework.authtoken.views import obtain_auth_token

# Django REST Framework Simple JWT
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

# Local imports
from user_app.api.views import logout_view, registration_view

urlpatterns = [
    # Token authentication
    path('login/', obtain_auth_token, name='login'),
    path('register/', registration_view, name='register'),
    path('logout/', logout_view, name='logout'),
    # JWT authentication
    # path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
