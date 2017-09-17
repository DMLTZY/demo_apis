from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsSuperuser(BasePermission):
    message = 'You are not superuser'

    def has_object_permission(self, request, view, obj):
        return request.user.is_superuser


class IsAdminOrOwner(BasePermission):
    message = 'You are not admin or owner'

    def has_object_permission(self, request, view, obj):
        return request.user.is_superuser or obj == request.user


class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS

