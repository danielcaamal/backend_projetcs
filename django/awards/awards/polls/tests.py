# Python
import datetime, django, os

# Django
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

# Local
from .models import Question

# Create your tests here.
class QuestionModelTest(TestCase):
    
    # Testing functions
    def test_was_published_recently_with_past_questions(self):
        '''was_published_recently returns False for questions whose pub_date is at least one day ago'''
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        past_question = Question(pub_date=time, text='Is this a past testing question?')
        self.assertIs(past_question.was_published_recently(), False)
    
    def test_was_published_recently_with_recently_questions(self):
        '''was_published_recently returns True for questions whose pub_date is max one day ago'''
        time = timezone.now() - datetime.timedelta(hours=12)
        recently_question = Question(pub_date=time, text='Is this a recently testing question?')
        self.assertIs(recently_question.was_published_recently(), True)
    
    def test_was_published_recently_with_future_questions(self):
        '''was_published_recently returns False for questions whose pub_date is in the future'''
        time = timezone.now() + datetime.timedelta(days=1, seconds=1)
        future_question = Question(pub_date=time, text='Is this a future testing question?')
        self.assertIs(future_question.was_published_recently(), False)



def create_question(text, days):
    '''
    Create a question with the given question "text", and published the given
    number of days offset to now (negative for questions published in the past,
    positive for questions that have yet to be published)
    '''
    time = timezone.now() + datetime.timedelta(days=days)
    question = Question(text=text, pub_date=time)
    question.save()
    return question
class QuestionIndexViewTest(TestCase):
    def test_no_questions(self):
        '''If not question exist, an appropriate message is displayed'''
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'No polls available.')
        self.assertQuerysetEqual(response.context['latest_question_list'], [])
        
    def test_questions_with_future_pub_date(self):
        '''If there are questions in the future, are not going to be showed'''
        
        # Create questions
        recently_question = create_question('Is this a recently testing question?', 0)
        future_question = create_question('Is this a future testing question?', 30)

        # Get Response
        response = self.client.get(reverse('polls:index'))
        
        # Validations
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, recently_question.text)
        self.assertNotContains(response, future_question.text)
        
    def test_questions_with_past_pub_date(self):
        '''If there are questions in the past, then are going to be showed'''
        # Create questions
        recently_question = create_question('Is this a recently testing question?', 0)
        past_question = create_question('Is this a past testing question?', -30)

        # Get Response
        response = self.client.get(reverse('polls:index'))
        
        # Validations
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, recently_question.text)
        self.assertContains(response, past_question.text)
        
    def test_questions_with_past_pub_date(self):
        '''The questions index page may display multiples questions'''
        past_question_1 = create_question('Is this a past testing question_1', -60)
        past_question_2 = create_question('Is this a past testing question_2?', -30)

        # Get Response
        response = self.client.get(reverse('polls:index'))
        
        # Validations
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, past_question_1.text)
        self.assertContains(response, past_question_2.text)
        
class QuestionDetailViewTest(TestCase):
    def test_future_question(self):
        '''
        The detail view of a question with a pub date in the future
        returns a 404 error not found.
        '''
        future_question = create_question('Is this a future testing question?', 30)
        url = reverse('polls:detail', args=(future_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
    
    def test_past_question(self):
        '''
        The detail view of a question with a pub date in the past
        displays the question detail.
        '''
        past_question = create_question('Is this a past testing question', -60)
        url = reverse('polls:detail', args=(past_question.id,))
        response = self.client.get(url)
        self.assertContains(response, past_question.text)