from rest_framework import permissions




"""
custom permissions author only access for endpoint GET, POST, PUT, DELETE
"""

class IsAuthorOrReadOnly(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user


