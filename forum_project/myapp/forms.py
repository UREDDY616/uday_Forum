from django import forms

from .models import Answer,Question



class QuestionForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = ('author','title','text')



class AnswerForm(forms.ModelForm):

    class Meta:
        model = Answer
        fields = ('author','text')

