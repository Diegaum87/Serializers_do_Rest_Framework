from rest_framework import serializers
from recipes.serializers import RecipeSerializer


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField(max_length=15)
    last_name = serializers.CharField(max_length=15)
    email = serializers.EmailField()

    # auto_now_add -> Atualização no momento de criação do dado
    created_at = serializers.DateTimeField(read_only=True)
    # auto_now -> Atualização no momento de atualização do dado
    updated_at = serializers.DateTimeField(read_only=True)

    recipes = RecipeSerializer(many=True, read_only=True)
