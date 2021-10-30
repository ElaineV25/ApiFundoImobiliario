from rest_framework import serializers
from api.models import FundoImobiliario

class FundoImobiliarioSerializer(serializers.ModelSerializer):
    class Meta:
        fields = [
            'id',
            'codigo',
            'setor',
            'dividend_financeira',
            'vacancia_fisica',
            'quantidade_ativos'
        ]
