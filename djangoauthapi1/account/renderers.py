from email import charset
from rest_framework import renderers
import json
# to show ta error in the custom way
class UserRenderer(renderers.JSONRenderer):
    charset = 'utf-8'
    def render(self, data, accepted_media_type=None, renderer_context = None):
        response = ''
        if 'ErrorDetail' in str(data):
            response = json.dumps({'errors' : data})
        else:
            response = json.dumps(data)
        return response