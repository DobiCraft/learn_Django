from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

from django.db import models

# Create your models here.
@python_2_unicode_compatible
class Bookmark(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    url = models.URLField('url', unique=True)

    #def __unicode__(self):
    def __str__(self): #�ν��Ͻ� ��½� ��ȯ�ϴ� ������ ���¸� ����. print(object)�� title�� �����.
        return self.title