from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Lesson(models.Model):
    lessonName = models.CharField(max_length=255)
    def __str__(self):
        return self.lessonName 

class LJTTCard(models.Model):
    imageData = models.TextField()
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    jp_word = models.TextField()
    en_word = models.TextField()
    en_pronounciation = models.TextField()
    ta_word = models.TextField()
    ta_pronounciation = models.TextField()
    hint = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="LJTTCard")
    likes = models.ManyToManyField(User, related_name='ljtt_cards')

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.jp_word + ' | ' +  self.en_word + ' | ' + self.en_pronounciation

    def get_absolute_url(self):
        return reverse('cards.detail', args=(self.pk, ))
