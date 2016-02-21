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


class GroupSerializer(serializers.ModelSerializer):
    """Serializer for complete representation of a group record."""

    users = serializers.SlugRelatedField(
        many=True,
        queryset=User.objects,
        slug_field='userid')

    class Meta:
        model = Group
        fields = ('name', 'users')


class NewGroupSerializer(serializers.ModelSerializer):
    """New groups are created empty: only a 'name' value is required."""

    class Meta:
        model = Group
        fields = ('name',)
