from rest_framework import serializers
from portfolio.models import User, Project

class UserSerializer(serializers.ModelSerializer):
    project_count = serializers.SerializerMethodField('get_project_count')
    user_project_count = serializers.SerializerMethodField('get_user_project_count')
    user_token = serializers.SerializerMethodField('get_user_token')
    class Meta:
        model = User
        fields = ('id', 'user_token', 'username', 'first_name', 'last_name', 'user_project_count', 'user_project_count', 'email', 'is_staff', 'date_joined', 'about', 'password')
        read_only_fields = ('date_joined', 'username')

    def get_project_count(self, obj):
        return obj.project.count()

    def get_user_project_count(self, obj):
        return 0

    def get_user_token(self, obj):
        return obj.auth_token

    def validate_password(self, attrs, source):
        """
        Check that the password created is longer than 4 characters
        """
        password = attrs[source]
        if len(password)<4:
            raise serializers.ValidationError("SHORT!")
        return attrs


class ProjectSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)

    class Meta:
        model = Project

