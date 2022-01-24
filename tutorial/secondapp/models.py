from django.db import models

class ArmyShop(models.Model):
    year=models.IntegerField()
    month=models.IntegerField()
    type=models.TextField()
    name=models.TextField()
    class Meta:
        db_table = 'army_shop'
        app_label= 'secondapp'
        ##-id -> 아이디 내림차순 (역순)
        ordering=['-id','year','month','type','name']
        managed=False
# 1. 클래스
# 2. 모델 상속 (그래야 데이터 상속받는지 암)
# 3. 속성 => 변수 => 000Field 대입
class Course(models.Model):
    name = models.CharField(max_length=30)
    cnt = models.IntegerField()
    