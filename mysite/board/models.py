from pickle import TRUE
from typing_extensions import Required
from django.db import models


class Review(models.Model):
    #author = models.ForeignKey(User, on_delete=models.CASCADE,related_name='author_review')
    subject = models.CharField(max_length=255)
    content = models.TextField()
    file=models.FileField(upload_to='%Y/%m/%d',null=True,blank=True)
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    #voter = models.ManyToManyField(User,related_name='voter_review')
    
    def __str__(self):
        return self.subject

class Comment(models.Model):
    #author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_comment')
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    #voter = models.ManyToManyField(User, related_name='voter_comment')

    def __str__(self):
        return self.title