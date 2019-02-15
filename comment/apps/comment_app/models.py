from __future__ import unicode_literals
from django.db import models
import re, bcrypt
from datetime import datetime
from ..app_one.models import *
from . models import *

# Create your models here.

class QuoteManager(models.Manager):
    def quote_validator(self, postData):
        errors = {}
        if len(postData['author']) < 3:
            errors['authorlength'] = "Please enter author (must be at least 3 characters)."
        if len(postData['quote']) < 10:
            errors['quotelength'] = "Please enter quote (must be at least 10 characters)."

        return errors


class Quote(models.Model):
    author = models.CharField(max_length = 255)
    quote = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    user_quote = models.ForeignKey(User, related_name = 'quote_created', on_delete = 'models.CASCADE')
    user_like = models.ManyToManyField(User, related_name = 'quote_like')
    objects = QuoteManager()