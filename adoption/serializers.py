from rest_framework import serializers

from pet.models import Pet
from pet.serializers import PetSerializer
from .models import Adoption


class AdoptionSerializer(serializers.ModelSerializer):
    pet = PetSerializer(many=False, read_only=True)
    pet_id = serializers.PrimaryKeyRelatedField(
        many=False,
        write_only=True,
        queryset= Pet.objects.all()
    )

    class Meta:
        model = Adoption
        fields = ('id', 'value', 'email', 'pet', 'pet_id')

    def create(self, validated_data):
        validated_data['pet'] = validated_data.pop('pet_id')
        return super().create(validated_data)

    def validate_value(self, value):
        if value < 0:
            raise serializers.ValidationError('Must be a positive value')
        return value