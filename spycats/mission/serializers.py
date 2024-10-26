from datetime import datetime
from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField, ValidationError
from .models import Cat, Mission, Target

class TargetSerializer(ModelSerializer):
    class Meta:
        model = Target
        fields = ['name', 'country', 'notes', 'complete']

    def validate_notes(self, note):
        if not isinstance(note, str):
            try:
                note = str(note)
            except TypeError:
                raise ValidationError("Cannot convert note to a string")
        if self.instance.complete:
            raise ValidationError("Cannot update notes as the target is already completed.")
        if self.instance.mission.complete:
            raise ValidationError("Cannot update notes as the mission is already completed.")
        date = datetime.now().strftime()
        return {date: note}
    
    def update(self, instance, validated_data):
        if 'notes' in validated_data:
            notes = instance.notes or {} 
            new_notes = validated_data.pop('notes')
            notes.update(new_notes)
            instance.notes = notes
        return super().update(instance, validated_data)

class MissionSerializer(ModelSerializer):
    targets = TargetSerializer(many=True)
    cat_id = PrimaryKeyRelatedField(queryset=Cat.objects.all(), source='cat')

    class Meta:
        model = Mission
        fields = ['cat_id', 'complete', 'targets']

    def create(self, validated_data):
        targets = validated_data.pop('targets')
        mission = Mission.objects.create(**validated_data)
        
        for target in targets:
            Target.objects.create(mission=mission, **target)
        return mission