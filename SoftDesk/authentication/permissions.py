from rest_framework.permissions import BasePermission, SAFE_METHODS


# Here we are doing something that is just a customization of the application.
# This has_object method already works on an existing object, so SAFE_METHODS are already handled by Django REST.
# Unlike the same case for a new object, it cannot perform POST requests.
class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        else:
            return obj == request.user