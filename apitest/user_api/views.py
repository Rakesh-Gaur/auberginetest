from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from user_api.serializers import UserSerializer , UrlSerializer
from rest_framework.authtoken.models import Token


class UserCreate(APIView):
    """
    Creates the user.
    """

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                token = Token.objects.create(user=user)
                json = serializer.data
                json['token'] = token.key
                return Response(json, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view()
def error_view(request):
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view()
def verified_view(request):
    return Response("Email account is activated")


@api_view(['POST'])
def save_url_image(request):
    serializer = UrlSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)
    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

