from rest_framework import serializers
from .models import Cpf


class CpfSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cpf
        fields = ['number', 'status']
