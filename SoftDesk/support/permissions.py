from rest_framework.permissions import BasePermission, SAFE_METHODS
 
class IsAdminAuthenticated(BasePermission):
 
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.is_superuser)
    
class IsContributorAuthenticated(BasePermission):
 
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.is_superuser)
    
class IsAuthorOrReadOnly(BasePermission):

    # Applies to the object. SAFE_METHODS are the actions allowed for read-only users.
    # For example, with a GET request on the object, even somebody else than the author can still view it.
    # The first True allows the first action.
    # In the else case, if the condition is met it returns True, otherwise False.
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        else:
            return obj.author == request.user

