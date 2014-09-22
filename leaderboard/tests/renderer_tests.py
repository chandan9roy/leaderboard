from django.contrib.auth.models import User
from django.test import SimpleTestCase
import json
from mock import Mock, patch

from leaderboards.api.renderers import RequireJSRenderer


class RequireJSRendererTest(SimpleTestCase):
    def test_get_model_name(self):
        """
        Verifies that a model name is returned if a renderer context has a queryset
        """
        renderer_context = {
            'view': Mock(queryset=User.objects.all())
        }
        self.assertEqual('user', RequireJSRenderer().get_model_name(renderer_context))

    def test_get_model_name_null(self):
        """
        Verifies that None is returned if context rendered is invalid
        """
        self.assertIsNone(RequireJSRenderer().get_model_name(None))

    @patch('leaderboards.api.renderers.RequireJSRenderer.get_model_name', spec_set=True)
    @patch('rest_framework.renderers.JSONRenderer.render', spec_set=True)
    def test_render(self, mock_render, mock_get_model_name):
        """
        Verifies that the rendered returns the expected data
        :type mock_render: Mock
        :type mock_get_model_name: Mock
        """
        mock_get_model_name.return_value = 'Test'
        mock_render.return_value = json.dumps({'one': 'two'})

        render_value = RequireJSRenderer().render('data', media_type='media_type', renderer_context='renderer_context')
        mock_render.assert_called_with('data', 'media_type', 'renderer_context')
        expected_str = 'define("Test",function(){return {"one": "two"};});'

        self.assertEqual(expected_str, render_value)
