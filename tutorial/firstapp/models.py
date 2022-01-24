from django.db import models

class Curriculum(models.Model):
    name = models.CharField(max_length=255)
    #오버라이딩 : 다형성 때문에 함
    def __str__(self):
        return self.name
        
class Course(models.Model):
    name = models.CharField(max_length=30)
    cnt = models.IntegerField()
    