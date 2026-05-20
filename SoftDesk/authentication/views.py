from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.exceptions import PermissionDenied

from authentication.models import User
from authentication.serializers import UserSerializer, UserListSerializer
from authentication.permissions import IsOwnerOrReadOnly


class UserViewset(ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_queryset(self):
        return User.objects.all()

    # To retrieve data inside the perform methods, we use the serializer and validated_data.
    # The perform_create method already exists, I need to use it here.
    def perform_create(self, serializer):
        age = serializer.validated_data['age']
        if int(age) >= 15:
            user = serializer.save()
            user.set_password(user.password)
            user.save()
        else:
            raise PermissionDenied("Il faut avoir au moins 15 ans pour créer un compte.")

    # The 'list' action is a get request, provided by Django.
    def get_serializer_class(self):
        if self.action == 'list':
            self.serializer_class = UserListSerializer
        else:
            self.serializer_class = UserSerializer
        return self.serializer_class

    # Function triggered when retrieving a single user, provided by Django.
    # super() calls the parent method implementation
    # The retrieve method already exists, I need to use it here.
    def retrieve(self, request, *args, **kwargs):
        user = self.get_object()
        if user.can_data_be_shared or user == request.user:
            return super().retrieve(request, *args, **kwargs)
        else:
            raise PermissionDenied("Les données de cet utilisateur ne sont pas partagées.")