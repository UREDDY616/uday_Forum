
from django.conf.urls import url
from . import views

# Create your views here.


urlpatterns = [
       url(r'^$',views.QuestionListView.as_view(),name='question_list'),
       url(r'^question/(?P<pk>\d+)$',views.QuestionDetailView.as_view(),name= 'question_detail'),
       url(r'^question/new/$',views.CreateQuestionView.as_view(),name='question_new'),
       url(r'^drafts/$',view.DraftListView.as_view(),name='question_draft_list'),
       url(r'^question/(?P<pk>\d+)/remove/$',views.QuestionDeleteView.as_view(),name='question_remove'),
       url(r'^question/(?P<pk>\d+)/publish/$',views.question_publish,name='question_publish'),
       url(r'^question/(?P<pk>\d+)/answer/$',views.add_answer_to_question,name='add_answer_to_question'),
       url(r'^answer/(?P<pk>\d+)/approve/$',views.answer_approve,name='answer_approve'),
       url(r'^answer/(?P<pk>\d+)/remove/$',views.answer_remove,name='answer_remove')
]
