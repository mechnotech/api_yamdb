from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return (request.method in permissions.SAFE_METHODS
                or obj.author == request.user)


class IsSelfOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj == request.user or request.user.role == 'admin'


class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        if bool(request.user.is_authenticated):
            if request.user.role == 'admin' or request.user.is_staff:
                return True
        return False

    def has_object_permission(self, request, view, obj):
        if bool(request.user.is_authenticated):
            if request.user.role == 'admin' or request.user.is_staff:
                return True
        return False
