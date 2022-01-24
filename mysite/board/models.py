from django.db import models


class Review(models.Model):
    #author = models.ForeignKey(User, on_delete=models.CASCADE,related_name='author_question')
    subject = models.CharField(max_length=255)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    #voter = models.ManyToManyField(User,related_name='voter_question')
    
    def __str__(self):
        return self.subject

class Answer(models.Model):
    #author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_answer')
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    #voter = models.ManyToManyField(User, related_name='voter_answer')

