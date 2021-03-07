from rest_framework import serializers
from ..models.roles import Role


class RoleSerializer(serializers.ModelSerializer):
    """"""
    class Meta:
        model = Role
        fields = '__all__'
