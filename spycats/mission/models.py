from django.db import models as m
from cats.models import Cat

class Mission(m.Model):
    cat = m.ForeignKey(Cat, on_delete=m.CASCADE, related_name='missions')
    complete = m.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.pk is not None:
            prev = Mission.objects.get(pk=self.pk)
            if self.complete and prev.complete != self.complete:
                self.targets.update(complete=True)
        super().save(*args, **kwargs)

class Target(m.Model):
   name = m.CharField(max_length=15) 
   country = m.CharField()
   notes = m.JSONField(null=True)
   complete = m.BooleanField(default=False)
   mission = m.ForeignKey(Mission, on_delete=m.CASCADE, related_name='targets')