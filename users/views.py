from django.core.mail import send_mail
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from users.serializers import YamRegUserSerializer


class Token(APIView):
    # permission_classes = [permissions.IsAuthenticated]

    # def get(self, request, format=None):
    #     polls = Poll.objects.all()
    #     serializer = PollSerializer(polls, many=True)
    #     return Response(serializer.data)

    def post(self, request, format=None):
        email = request.data['email']
        serializer = YamRegUserSerializer(data={'email': email})

        if serializer.is_valid():
            serializer.save(username=email)
            code = 123
            send_mail(
                'Confirmation Code',
                f'Hi, there. This is your code: {code}',
                'from@example.com',
                [email],
                fail_silently=False,
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

