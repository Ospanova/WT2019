from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=250)
    body = models.CharField(max_length=250)
    like_count = models.IntegerField(max_length=250)
    created_at = models.DateTimeField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=2)


    def __str__(self):
        return '{}: {}'.format(self.title, self.body, self.like_count)

    def to_json(self):
        return {
            'id': self.id,
            'title': self.title,
            'body' : self.body,
            'like_count' : self.like_count,
        }
