from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

from django.db import models

# Create your models here.
@python_2_unicode_compatible
class Bookmark(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    url = models.URLField('url', unique=True)

    #def __unicode__(self):
    def __str__(self): #인스턴스 출력시 반환하는 데어터 형태를 지정. print(object)시 title을 출력함.
        return self.title