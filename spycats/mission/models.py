from django.db import models as m
from cats.models import Cat

class Mission(m.Model):
    cat = m.ForeignKey(Cat, on_delete=m.CASCADE, related_name='missions')
    complete = m.BooleanField(default=False)

class Target(m.Model):
   name = m.CharField(max_length=15) 
   country = m.CharField()
   notes = m.JSONField(null=True)
   complete = m.BooleanField(default=False)
   mission = m.ForeignKey(Mission, on_delete=m.CASCADE, related_name='targets')