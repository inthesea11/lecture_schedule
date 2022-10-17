from django.db import models

from django.urls import reverse

class Subject(models.Model):
    sub_name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
# Create your models here.


    def __str__(self):
        return "과 : "+self.department+" , 과정 :  "+self.sub_name

    def get_absolute_url(self):
        return reverse('detail', args=[str(self.id)])