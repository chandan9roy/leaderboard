from __future__ import unicode_literals
from rest_framework import renderers


class RequireJSRenderer(renderers.BaseRenderer):
    media_type = 'application/javascript'
    format = 'js'

    def get_model_name(self, renderer_context):
        if renderer_context and 'view' in renderer_context and hasattr(renderer_context['view'], 'queryset'):
            return renderer_context['view'].queryset.model.__name__.lower()
        return None

    def render(self, data, media_type=None, renderer_context=None):
        model_name = self.get_model_name(renderer_context)
        json_str = renderers.JSONRenderer().render(data, media_type, renderer_context)
        return 'define("{0}",function(){{return {1};}});'.format(model_name, json_str)
