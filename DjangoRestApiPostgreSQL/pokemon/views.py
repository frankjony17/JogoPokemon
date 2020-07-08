from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from pokemon.models import Pokemon
from pokemon.models import Tipo
from pokemon.serializers import PokemonSerializer, TipoSerializer
from rest_framework.decorators import api_view


@api_view(['GET'])
def find_all(request):
    pokemon_list = Pokemon.objects.all()
    pokemon_serializer = PokemonSerializer(pokemon_list, many=True)
    return JsonResponse(pokemon_serializer.data, safe=False)


@api_view(['GET'])
def find_tipo_all(request):
    tipo_list = Tipo.objects.all()
    tipo_serializer = TipoSerializer(tipo_list, many=True)
    return JsonResponse(tipo_serializer.data, safe=False)


@api_view(['GET'])
def find_by_id(request, pk):
    try:
        pokemon = Pokemon.objects.get(pk=pk)
        pokemon_serializer = PokemonSerializer(pokemon)
        return JsonResponse(pokemon_serializer.data)
    except Pokemon.DoesNotExist:
        return JsonResponse(
            {'message': 'The pokemon does not exist'},
            status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def find_by_name(request):
    pokemons = Pokemon.objects.all()
    nome = request.GET.get('nome', None)
    if nome is not None:
        pokemons = pokemons.filter(name__icontains=nome)

    pokemon_serializer = PokemonSerializer(pokemons, many=True)
    return JsonResponse(pokemon_serializer.data, safe=False)


@api_view(['POST'])
def create(request):
    pokemon_data = JSONParser().parse(request)
    pokemon_serializer = PokemonSerializer(data=pokemon_data)
    if pokemon_serializer.is_valid():
        pokemon_serializer.save()
        return JsonResponse(
            pokemon_serializer.data, status=status.HTTP_201_CREATED
        )
    return JsonResponse(
        pokemon_serializer.errors, status=status.HTTP_400_BAD_REQUEST
    )


@api_view(['PUT'])
def update(request, pk):
    try:
        pokemon = Pokemon.objects.get(pk=pk)
        pokemon_data = JSONParser().parse(request)
        pokemon_serializer = PokemonSerializer(pokemon, data=pokemon_data)

        if pokemon_serializer.is_valid():
            pokemon_serializer.save()
            return JsonResponse(pokemon_serializer.data)

        return JsonResponse(
            pokemon_serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )
    except Pokemon.DoesNotExist:
        return JsonResponse({'message': 'The pokemon does not exist'},
                            status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def delete(request, pk):
    try:
        pokemon = Pokemon.objects.get(pk=pk)
        pokemon.delete()
        return JsonResponse({'message': 'pokemon was deleted successfully!'},
                            status=status.HTTP_204_NO_CONTENT)
    except Pokemon.DoesNotExist:
        return JsonResponse({'message': 'The pokemon does not exist'},
                            status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def delete_all(request):
    count = Pokemon.objects.all().delete()
    return JsonResponse(
        {'message': '{} Pokemons were deleted successfully!'.format(count[0])},
        status=status.HTTP_204_NO_CONTENT)
