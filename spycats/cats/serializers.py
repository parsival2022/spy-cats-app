import requests as r
from .models import Cat
from rest_framework.serializers import ModelSerializer, ValidationError

class CatSerializer(ModelSerializer):
    class Meta:
        model = Cat
        fields = "__all__"
    
    def validate_breed(self, breed):
        breeds_res = r.get("https://api.thecatapi.com/v1/breeds")
        breeds = [b["name"] for b in breeds_res.json()]
        if not breed in breeds: 
            raise ValidationError("This breed is unknown or misspelled")
        return breed

