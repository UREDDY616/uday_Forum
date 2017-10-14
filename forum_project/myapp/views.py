from django.shortcuts import render,get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from myapp.models import Question,Answer
from django.utils import timezone
from myapp.forms import QuestionForm,AnswerForm
from django.views.generic import   (TemplateView,ListView,
                                     DetailView,CreateView,
                                     UpdateView,DeleteView)
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class QuestionListView(ListView):
    model = Question

    def get_queryset(self):
        return Question.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')


class QuestionDetailView(DetailView):
    model = Question

class  CreateQuestionView(LoginRequiredMixin,CreateView):
    login_url = '/login/'

    redirect_field_name = 'myapp/question_detail.html'

    form_class = QuestionForm

    model = Question


class DraftListView(LoginRequiredMixin,ListView):
    login_url = '/login/'
    redirect_field_name = 'myapp/question_list.html'

    model = Question

    def get_queryset(self):
        return Question.objects.filter(published_date__isnull = True).order_by('created_date')


class QuestionDeleteView(LoginRequiredMixin,DeleteView):
    model = Question

    success_url = reverse_lazy('question_list')

 
