from rest_framework import serializers

from parent.models import Parent
from baby.models import Baby

class ParentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parent
        fields = (
            'id',
            'name',
            'babies'
        )