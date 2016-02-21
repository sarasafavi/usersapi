from users.models import ApiUser, ApiGroup
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    groups = serializers.SlugRelatedField(
        many=True,
        queryset=ApiGroup.objects.all(),
        slug_field='name')

    class Meta:
        model = ApiUser
        fields = ('first_name', 'last_name', 'userid', 'groups')


class GroupSerializer(serializers.ModelSerializer):
    """Serializer for complete representation of a group record.
    """

    users = serializers.SlugRelatedField(
        many=True,
        queryset=ApiUser.objects.all(),
        slug_field='userid')

    class Meta:
        model = ApiGroup
        fields = ('name', 'users')


class NewGroupSerializer(serializers.ModelSerializer):
    """New groups are created empty: only a 'name' value is required.
    """

    class Meta:
        model = ApiGroup
        fields = ('name',)
