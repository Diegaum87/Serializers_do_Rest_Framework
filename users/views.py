from rest_framework.views import APIView, Request, Response, status
from .models import User
from .serializers import UserSerializer


class UserView(APIView):
    def get(self, request: Request) -> Response:
        # QuerySet
        users = User.objects.all()

        # many=True é necessário quando passamos mais de um objeto para o serializer

        # Estamos formatando os dados para o retorno
        serializer = UserSerializer(instance=users, many=True)

        # serializer.data é para retorno
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request: Request) -> Response:
        # Valida os dados de entrada
        serializer = UserSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # serializer.validated_data é para quando formos criar
        user = User.objects.create(**serializer.validated_data)

        # Formata os dados para saida
        serializer = UserSerializer(instance=user)

        return Response(data=serializer.data, status=status.HTTP_201_CREATED)
