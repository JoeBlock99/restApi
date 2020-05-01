from rest_framework import serializers

from baby.models import Baby
from parent.serializers import ParentSerializer


class BabySerializer(serializers.ModelSerializer):
    events = serializer.StringRelatedField(many=True)


    class Meta:
        model = Baby
        fields = (
            'id',
            'name',
            'sex',
            'parent'
            'events'
        )
