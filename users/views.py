from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from users.models import ApiUser, ApiGroup
from users.serializers import (
    UserSerializer, GroupSerializer, NewGroupSerializer)


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
        users = ApiUser.objects.all()
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
            user = ApiUser.objects.get(userid=userid)
        except ApiUser.DoesNotExist:
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


class GroupList(APIView):
    """Allow creation of new groups. New groups are created by POSTing valid
    JSON with a "name" parameter:

    {"name": "new_group_name"}

    New groups may not be created with the same name as an existing group.
    """

    def get(self, request):
        # TODO this list-all-on-GET endpoint is not actually in spec
        groups = ApiGroup.objects.all()
        serializer = GroupSerializer(groups, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = NewGroupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GroupByName(APIView):
    """Allow access of groups by name. Permitted actions are:
    GET: returns the group and user IDs of any members
    PUT: update the group: requires a list of valid user IDs
    DELETE: delete the group"""

    def get_group(self, name):
        try:
            group = ApiGroup.objects.get(name=name)
        except ApiGroup.DoesNotExist:
            raise Http404
        return group

    def get(self, request, groupname):
        group = self.get_group(groupname)
        serializer = GroupSerializer(group)
        return Response(serializer.data)

    def put(self, request, groupname):
        group = self.get_group(groupname)
        update = {"users": request.data}  # spec wants list as request body
        serializer = GroupSerializer(group, update, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, groupname):
        group = self.get_group(groupname)
        group.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
