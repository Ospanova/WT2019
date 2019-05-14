from django.db import models
#from __future__ import unicode_literals
from django.contrib.auth.models import User
# Create your models here.


class ContactManager(models.Manager):
    def for_user(self, user):
        if (user.username == "admin"):
            return self.all()
        return self.filter(created_by=user)

class Contact (models.Model): 
    name  = models.CharField(max_length = 200)
    phone = models.CharField(max_length = 200)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=1)


    objects = ContactManager()

    def __str__(self):
        return{
            'id': self.id,
            'name': self.body,
            'phone': self.phone
        }

    def to_json(self):
        return {
            'id': self.id,
            'name': self.body,
            'phone': self.phone
        }

