from rest_framework.permissions import BasePermission

class CustomPermission(BasePermission):
    """
    A custom permission which allows the superuser access to all the methods (get, delete, update)
    while it allows a normal/not-logged in user to only the 'get' method
    """
    def has_permission(self, request, view):
        if request.user.is_superuser:
           return request.method in ['GET', 'POST', 'PUT', 'DELETE']
        else:
            return request.method in ['GET']
        
            
        