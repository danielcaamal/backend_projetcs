# Django
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404

# Django REST Framework
from rest_framework.authtoken.models import  Token
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Local imports 
from user_app.api.serializers import RegistrationSerializer

@api_view(['POST'])
# @csrf_exempt 
def registration_view(request):
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        response_data = {}
        
        serializer.is_valid(raise_exception=True)
        
        user = serializer.save()
        token = get_object_or_404(Token, user=user).key
        
        response_data = { **serializer.data, "token": token, "message": "User registered successfully" }
        
        return Response(response_data)


@api_view(['POST'])
def logout_view(request):
    if request.method == 'POST':
        request.user.auth_token.delete()
        return Response({ "message": "User logged out successfully" })