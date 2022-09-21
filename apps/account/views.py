from rest_framework import generics, views
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.account.serializers import UserSerializer


class LoginView(ObtainAuthToken):
    permission_classes = [~IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token, created = Token.objects.get_or_create(user=user)
        serializer = UserSerializer(user, many=False)
        resp = {
            **serializer.data,
            "token": token.key,
        }
        return Response(resp)


class LogoutView(views.APIView):
    def get(self, request):
        return Response({})


class UserMeView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user
