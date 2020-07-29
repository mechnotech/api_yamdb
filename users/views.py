from random import randint

from django.core.mail import send_mail
from django.db.models import ObjectDoesNotExist
from rest_framework import status, viewsets, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from users.models import YamUser
from users.permissions import IsAdmin
from users.serializers import YamRegUserSerializer, YamUsersSerializer, TokenSerializer


class UsersViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAdmin,)
    queryset = YamUser.objects.all()
    serializer_class = YamUsersSerializer


class UserViewSet(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAdmin,)
    pagination_class = None
    queryset = YamUser.objects.all()
    lookup_field = 'username'
    serializer_class = YamUsersSerializer




class EmailConfirmationCode(APIView):
    # permission_classes = [permissions.IsAuthenticated]

    # def get(self, request, format=None):
    #     polls = Poll.objects.all()
    #     serializer = PollSerializer(polls, many=True)
    #     return Response(serializer.data)

    def post(self, request):
        email = request.data['email']
        serializer = YamRegUserSerializer(data={'email': email})

        if serializer.is_valid():
            code = randint(100000, 999999)
            serializer.save(username=email, code=code)
            send_mail(
                'Confirmation Code',
                f'Hi, there. This is your code: {code}',
                'security@yamdb.fake',
                [email],
                fail_silently=False,
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Token(APIView):
    def post(self, request):
        email = request.data['email']
        code = int(request.data['code'])

        try:
            user = YamUser.objects.get(email=email)
        except ObjectDoesNotExist:
            user = None

        serializer = TokenSerializer(user, data=request.data)
        serializer.is_valid()
        if user is not None:
            if user.code == code:
                refresh = RefreshToken.for_user(user)
                return Response(data={'token': str(refresh.access_token)}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # return Response(data={'error': 'error', 'email': email, 'code': code}, status=status.HTTP_400_BAD_REQUEST)
