# Django
from django.urls import path

# Django REST Framework
from rest_framework.authtoken.views import obtain_auth_token

# Local imports
from user_app.api.views import logout_view, registration_view

urlpatterns = [
    path('login/', obtain_auth_token, name='login'),
    path('register/', registration_view, name='register'),
    path('logout/', logout_view, name='logout'),
    
]
