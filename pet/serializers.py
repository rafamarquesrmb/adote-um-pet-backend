from rest_framework import serializers

from pet.models import Pet


class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = ('id', 'name', 'bio_description', 'img_slug')
