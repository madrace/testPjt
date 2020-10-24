from django.db import models

# Create your models here.
class Memo(models.Model):
    title = models.CharField("제목", max_length=200)
    desc = models.TextField("본문", blank=True)
    
    createDate = models.DateTimeField((""), auto_now_add=True) # 생성시마다 fix됨
    modifyDate = models.DateTimeField((""), auto_now=True) # 수정시마다 변경됨

    def __str__(self):
        return self.title
