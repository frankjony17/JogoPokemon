from rest_framework import serializers
from pokemon.models import Pokemon, Tipo


class TipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tipo
        fields = ('id',
                  'name',
                  'slot',
                  'url')


class PokemonSerializer(serializers.ModelSerializer):
    tipo = TipoSerializer(many=False, required=True)

    class Meta:
        model = Pokemon
        fields = ('id',
                  'name',
                  'tamanho',
                  'ordem',
                  'tipo')

    def create(self, validated_data):
        pokemon_data = validated_data.pop('tipo')
        tipo = Tipo.objects.get(name=pokemon_data['name'])
        pokemon = Pokemon.objects.create(name=validated_data['name'],
                                         tamanho=validated_data['tamanho'],
                                         ordem=validated_data['ordem'],
                                         tipo=tipo)
        return pokemon

    def update(self, instance, validated_data):
        tipo_data = validated_data.pop('tipo')
        tipo = Tipo.objects.get(name=tipo_data['name'])
        instance.name = validated_data['name']
        instance.tamanho = validated_data['tamanho']
        instance.ordem = validated_data['ordem']
        instance.tipo = tipo
        instance.save()
        return instance

