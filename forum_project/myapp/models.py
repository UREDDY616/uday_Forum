from django.db import models

# Create your models here.
from django.db import models
from django.util import timezone
from django.core.urlresolvers import reverse
# Create your models here.


class Question(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default = timezone.now)
    published_date = models.DateTimeField(blank=True,null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def approve_answer(self):
        return self.comments.filter(approved_answer=True)

    def get_absolute_url(self):
        return reverse("question_detail",kwargs={'pk':self.pk})

    def __str__(self):
        return self.title



 class Answer(models.Model):
     question = models.ForeignKey('myapp.Question',related_name = 'Answers')
     author = moels.CharField(max_length= 200)
     text = modles.TextField()
     created_date = models.DateTimeField(default = timezone.now)
     approved_answer = models.BooleanField(default = False)

     def approve(self):
         self.approve_answer = True
         self.save
     def get_absolute_url(self):
         return reverse("question_list")

     def __str__(self):
         return self.text
