from rest_framework.permissions import SAFE_METHODS, BasePermission


class CreatorPermission(BasePermission):
    message = "Editing event is restricted to the author only."

    def has_object_permission(self, request, view, obj):

        if request.method in SAFE_METHODS:
            return True

        return obj.creator == request.user


# class IsAuthorOrReadOnly(BasePermission):
#     def has_object_permission(self, request, view, obj):
#         if request.method in SAFE_METHODS:
#             return True
#         return obj.user == request.user
