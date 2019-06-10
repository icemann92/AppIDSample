from django.http import HttpResponse
from rest_framework import viewsets
import json

class JWTView(viewsets.ReadOnlyModelViewSet):
    '''
        Simple view that returns the token on the Authorization header.
    '''

    def list(self, request):
        return HttpResponse(json.dumps(self.request.user.get_token()), content_type="application/json")
