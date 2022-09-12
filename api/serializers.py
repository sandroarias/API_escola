from rest_framework import serializers
from .models import Escola


class EscolaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Escola
        fields = ['id', 'nome', 'datanc', 'cpf']
