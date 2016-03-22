from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    dob = models.DateTimeField('date published')


class Topic(models.Model):
    name = models.CharField(max_length=60)

    
class Quote(models.Model):
    quote_text = models.CharField(max_length=200)
    authored_date = models.DateTimeField('date published')
    pub_date = models.DateTimeField('date published')
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)


