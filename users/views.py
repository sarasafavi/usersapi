from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from users.models import User
from users.serializers import UserSerializer


class UserList(APIView):
    """Allow creation of new user records. POST requests must include a
    complete user record in valid JSON. e.g.,:

        {
        "first_name": "Joe",
        "last_name": "Smith",
        "userid": "jsmith",
        "groups": ["admins", "users"]
        }

    All user record fields are required. Given user IDs must be unique, and
    any given groups must already exist.
    """

    def get(self, request):
        # TODO this list-all-on-GET endpoint is not actually in spec
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserById(APIView):
    """Allow access of users by user ID. Permitted actions are:
    GET: show the user record for this user ID
    PUT: update the user record; requires a valid user record
    DELETE: delete the user record at this user ID"""

    def get_user(self, userid):
        try:
            user = User.objects.get(userid=userid)
        except User.DoesNotExist:
            raise Http404
        return user

    def get(self, request, userid):
        user = self.get_user(userid)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, userid):
        user = self.get_user(userid)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, userid):
        user = self.get_user(userid)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

