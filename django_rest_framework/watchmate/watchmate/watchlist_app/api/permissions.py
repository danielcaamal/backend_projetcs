# Django REST Framework
from rest_framework import permissions

class IsAdminOrReadOnly(permissions.IsAdminUser):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            # Read permissions are allowed to any request,
            return True
        else:
            # Write permissions are only allowed to the owner of the review.
            return bool(request.user and request.user.is_staff)


class IsReviewUserOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            # Read permissions are allowed to any request,
            return True
        else:
            # Write permissions are only allowed to the owner of the review.
            return obj.review_user == request.user or request.user.is_staff