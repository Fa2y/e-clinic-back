from rest_framework import permissions


class DoctorPermission(permissions.BasePermission):
    """
    Global permission check for User role
    """

    message = "Only Doctor or Nurse is allowed to perform this action"

    def has_permission(self, request, view):
        user = request.user
        return user.role == "Doctor" or user.role == "Nurse" or user.role == "Admin"


class GRHPermission(permissions.BasePermission):
    """
    Global permission check for User role
    """

    message = "Only GRH is allowed to perform this action"

    def has_permission(self, request, view):
        user = request.user
        return user.role == "GRH" or user.role == "Admin"


class PatientPermission(permissions.BasePermission):
    """
    Global permission check for User role
    """

    message = "Only Patient is allowed to perform this action"

    def has_permission(self, request, view):
        user = request.user
        return user.role == "Patient" or user.role == "Admin"
