from django.db import models

# Create your models here.
class Question(models.Model):
    qusetion_text = models.CharField(max_length=200)
    publish_date = models.DateTimeField()

    def __str__(self):
        return self.qusetion_text

class Choice(models.Model):
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    question = models.ForeignKey(Question,models.CASCADE)
