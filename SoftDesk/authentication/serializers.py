from rest_framework.serializers import ModelSerializer
from authentication.models import User

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'last_name', 'first_name', 'email', 'password', 'can_be_contacted', 'can_data_be_shared', 'age']
        extra_kwargs = {
            'password' : {'write_only' : True}
        }

class UserListSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']
        