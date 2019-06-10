from rest_framework_jwt.authentication import JSONWebTokenAuthentication


class AuthenticatedServiceClient:
    ''''
    https://github.com/GetBlimp/django-rest-framework-jwt/issues/22#issuecomment-166451133
    '''

    def __init__(self, payload):
        self.token = payload

    def is_authenticated(self):
        return True

    def get_token(self):
        return self.token

class JwtServiceOnlyAuthentication(JSONWebTokenAuthentication):
    '''
        Override the JSONWebTokenAuthentication.authenticate_credentials method to not do user authentication.
        https://github.com/GetBlimp/django-rest-framework-jwt/issues/22
    '''
    def authenticate_credentials(self, payload):
        # Assign properties from payload to the AuthenticatedServiceClient object if necessary
        return AuthenticatedServiceClient(payload)