from users.models import User, Group
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    groups = serializers.SlugRelatedField(
        many=True,
        queryset=Group.objects,
        slug_field='name')

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'userid', 'groups')
