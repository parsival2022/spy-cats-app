from django.db import models as m

class Cat(m.Model):
    name = m.CharField(max_length=15)
    experience = m.IntegerField(null=True)
    breed = m.CharField(max_length=20)
    salary = m.IntegerField()

