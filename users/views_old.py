from rest_framework.views import APIView, Request, Response, status
from .models import User
from django.forms.models import model_to_dict


class UserView(APIView):
    def get(self, request: Request) -> Response:
        # QuerySet
        users = User.objects.all()

        user_list = []
        for user in users:
            user_dict = model_to_dict(user)
            user_dict["created_at"] = user.created_at
            user_dict["updated_at"] = user.updated_at
            user_dict["recipes"] = [
                model_to_dict(recipe) for recipe in user.recipes.all()
            ]
            user_list.append(user_dict)

        return Response(user_list, status.HTTP_200_OK)
