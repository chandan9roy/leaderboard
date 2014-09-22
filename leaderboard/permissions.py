from django.conf import settings
from django.contrib.auth.models import User
from rest_framework import permissions
from logging import getLogger
from requests import get, codes

logger = getLogger('django.request')


class IsAuthenticatedOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        try:
            auth_request = get(settings.AUTH_HOST, cookies=request.COOKIES)
            if auth_request.status_code == codes.ok:
                # Parse the user properties.
                user = auth_request.json()
                user_id = user['id']
                user_name = user['username']

                # Save a copy of the user if it doesn't exist.
                User.objects.get_or_create(id=user_id, username=user_name)

                # Always use the user id as the request's user value for convenience.
                immutable_hack = request.DATA.copy()
                immutable_hack['user'] = user_id
                request._data = immutable_hack

                return True
        except Exception, e:
            logger.error(e)
        return False
