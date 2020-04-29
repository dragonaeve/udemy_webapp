from django.db import models

# Create your models here.
class Quiz(models.Model):
	qid = models.AutoField("Quiz ID", primary_key=True)
	quiz_name = models.CharField(max_length=200)

class Question(models.Model):
	pid = models.AutoField("Problem ID", primary_key=True)
	qid = models.ForeignKey(Quiz, on_delete=models.CASCADE, verbose_name="Quiz ID")
	problem = models.CharField(max_length=1000)
	is_active = models.BooleanField(default=False)

class Answer(models.Model):
	aid = models.AutoField("Answer ID", primary_key=True)
	pid = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name="Problem ID")
	ans = models.CharField(max_length=1000)
	is_correct = models.BooleanField(default=False)

class UserAnswer(models.Model):
	qid = models.ForeignKey(Quiz, on_delete=models.CASCADE, verbose_name="Quiz ID")
	pid = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name="Problem ID")
	aid = models.ForeignKey(Answer, on_delete=models.CASCADE, verbose_name="Answer ID")
	is_correct = models.BooleanField(default=False)