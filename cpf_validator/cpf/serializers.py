from .models import Cpf
from rest_framework import serializers


class CpfSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cpf
        fields = ['number', 'status']