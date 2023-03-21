
# Create your models here.
from django.db import models
# Create your models here.
class Question(models.Model):

    question=models.CharField(max_length=100,null=True)
    marks=models.IntegerField(default=2)
    created_at=models.DateField(auto_now_add=True)
    updated_at=models.DateField(auto_now=True)

    def __str__(self):
        return self.question
    def getanswer(self):
        answer=Answer.objects.filter(question=self)
        data=[]
        for ans in answer:
            data.append({
                'answer':ans.answer,
                "correct":ans.iscorrect
            })
        return data

class Answer(models.Model):

    question=models.ForeignKey(Question,related_name='question_answer',on_delete=models.CASCADE)
    answer=models.CharField(max_length=100)
    iscorrect=models.BooleanField(default=False)
    created_at=models.DateField(auto_now_add=True)
    updated_at=models.DateField(auto_now=True)

    def __str__(self):
        return self.answer
