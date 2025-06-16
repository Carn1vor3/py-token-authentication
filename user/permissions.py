from rest_framework import permissions
from rest_framework.permissions import SAFE_METHODS


class IsAdminOrAuthenticatedReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user and request.user.is_staff:
            return True
        if ((request.method in SAFE_METHODS or request.method == "POST") and
                request.user and
                request.user.is_authenticated):
            return True
        return False
