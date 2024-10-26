from rest_framework import generics as g
from .models import Mission, Target
from .serializers import MissionSerializer, TargetSerializer, ValidationError

class MissionGetAllCreateView(g.ListCreateAPIView):
    queryset = Mission.objects.all()
    serializer_class = MissionSerializer

class MissionGetUpdateDeleteView(g.RetrieveUpdateDestroyAPIView):
    queryset = Mission.objects.all()
    serializer_class = MissionSerializer

    def perform_destroy(self, instance):
        if instance.cat:
            raise ValidationError("Cannot delete mission because it is assigned to a cat.", 400)
        instance.delete()

class TargetGetUpdateView(g.RetrieveUpdateAPIView):
    queryset = Target.objects.all()
    serializer_class = TargetSerializer