from django.test import SimpleTestCase
from django.http import HttpRequest
from rest_framework.request import Request
from leaderboards.permissions import IsAuthenticatedOrReadOnly
from mock import patch
from requests import codes, ConnectionError


class IsAuthenticatedTest(SimpleTestCase):
    def test_handle_good_response_get(self):
        request = HttpRequest()
        request.method = 'GET'
        real = IsAuthenticatedOrReadOnly()
        self.assertTrue(real.has_permission(request, None))

    @patch('leaderboards.permissions.User')
    @patch('leaderboards.permissions.get')
    def test_handle_good_response_post(self, mock_get, mock_user):
        mock_get.return_value.status_code = codes.ok
        request = HttpRequest()
        request.method = 'POST'
        request = Request(request)
        real = IsAuthenticatedOrReadOnly()
        self.assertTrue(real.has_permission(request, None))

    @patch('leaderboards.permissions.get')
    def test_handle_bad_response(self, mock_get):
        mock_get.return_value.status_code = codes.unauthorized
        request = HttpRequest()
        real = IsAuthenticatedOrReadOnly()
        self.assertFalse(real.has_permission(request, None))

    @patch('leaderboards.permissions.get')
    def test_handle_error_response(self, mock_get):
        mock_get.side_effect = ConnectionError('pretend failing to connect')
        request = HttpRequest()
        real = IsAuthenticatedOrReadOnly()
        self.assertFalse(real.has_permission(request, None))
