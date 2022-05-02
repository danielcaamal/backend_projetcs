# Django
from platform import platform
from django.contrib.auth.models import User
from django.urls import reverse

# Django REST Framework
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token

# Local imports
from watchlist_app import models
from watchlist_app.api import serializers


class StreamPlatformTestCase(APITestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(username='test_user', password='test_password')
        self.token = Token.objects.get(user__username=self.user.username)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        
        self.stream = models.StreamPlatform.objects.create(
            name="Netflix",
            about="Watch movies and TV shows online",
            website="https://www.netflux.com/",
        )
    
    def test_streamplatform_create_unauthorized(self):
        data = {
            "name": "Netflix",
            "about": "Watch movies and TV shows online",
            "website": "https://www.netflux.com/",
        }
        response = self.client.post(reverse('streamplatform-list'), data)
        
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        
    
    def test_streamplatform_list(self):
        response = self.client.get(reverse('streamplatform-list'))
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_streamplatform_ind(self):
        response = self.client.get(reverse('streamplatform-detail', kwargs={'pk': self.stream.id}))
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        

class WatchlistTestCase(APITestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(username='test_user', password='test_password')
        self.token = Token.objects.get(user__username=self.user.username)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        
        self.stream = models.StreamPlatform.objects.create(
            name="Netflix",
            about="Watch movies and TV shows online",
            website="https://www.netflux.com/",
        )
        
        self.watchlist = models.Watchlist.objects.create(
            platform=self.stream,
            title="The Witcher",
            storyline="The Witcher is a story of Geralt of Rivia, a monster hunter, who is drawn to the monster known as the Feral Child.",
            active=True
        )
        
    def test_watchlist_create_unauthorized(self):
        data = {
            "platform": self.stream.id,
            "title": "The Witcher",
            "storyline": "The Witcher is a story of Geralt of Rivia, a monster hunter, who is drawn to the monster known as the Feral Child.",
            "active": True,
        }
        response = self.client.post(reverse('watchlist'), data)
        
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        
    def test_watchlist_list(self):
        response = self.client.get(reverse('watchlist'))
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_watchlist_ind(self):
        response = self.client.get(reverse('watchlist-details', kwargs={'pk': self.watchlist.id}))
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class ReviewTestCase(APITestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(username='test_user', password='test_password')
        self.token = Token.objects.get(user__username=self.user.username)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        
        self.stream = models.StreamPlatform.objects.create(
            name="Netflix",
            about="Watch movies and TV shows online",
            website="https://www.netflux.com/",
        )
        
        self.watchlist = models.Watchlist.objects.create(
            platform=self.stream,
            title="The Witcher",
            storyline="The Witcher is a story of Geralt of Rivia, a monster hunter, who is drawn to the monster known as the Feral Child.",
            active=True
        )
    
    def test_review_create(self):
        data = {
            "review_user": self.user,
            "rating": 5,
            "description": "This is a great movie",
            "watchlist": self.watchlist.id,
            "active": True,
        }
        # response = self.client.post(reverse('review-create'), kwargs={"pk":self.watchlist.id}, data=data)
        
        # self.assertEqual(response.status_code, status.HTTP_201_CREATED)