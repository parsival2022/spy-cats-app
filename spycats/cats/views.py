from rest_framework import generics as g
from .models import Cat
from .serializers import CatSerializer

class CatGetAllCreateView(g.ListCreateAPIView):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer

class CatGetUpdateDeleteView(g.RetrieveUpdateDestroyAPIView):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer