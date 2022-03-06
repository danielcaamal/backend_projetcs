from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from .models import Question, Choice
from django.views.generic import  ListView, DetailView


# Class Base Views
class IndexView(ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'
    def get_queryset(self):
        '''Return last five published questions'''
        return Question.objects.order_by('-pub_date')[:5]

class DetailView(DetailView):
    model = Question
    template_name = 'polls/detail.html'

class ResultView(DetailView):
    model = Question
    template_name = 'polls/results.html'

# Class Base Functions

# def index(request):
#     context = {}
#     context['latest_question_list'] = Question.objects.all()
#     return render(request, 'polls/index.html', context=context)

# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     context = {
#         'question': question
#     }
#     return render(request, 'polls/detail.html', context=context)

# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {
#         'question': question
#     })

def vote(request, question_id):
    if request.method == 'POST':
        question = get_object_or_404(Question, pk=question_id)
        try:
            selected_choice = question.question_choices.get(pk=request.POST['choice']) # name input
        except (KeyError, Choice.DoesNotExist):
            return render(request, 'polls/detail.html', {
                'question': question,
                'error_message': 'No elegiste una respuesta valida.'
            })
        else:
            selected_choice.votes += 1
            selected_choice.save()
            return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
