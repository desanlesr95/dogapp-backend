from rest_framework_simplejwt.tokens import AccessToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.contrib.auth.models import User
from django.http import HttpResponseForbidden
from datetime import datetime, timedelta
import jwt
from django.conf import settings
from django.contrib.auth import get_user_model
from api.models import User
from rest_framework import authentication
from rest_framework.exceptions import AuthenticationFailed, ParseError



class JWTAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        # Extract the JWT from the Authorization header
        jwt_token = request.META.get('HTTP_AUTHORIZATION')
        if jwt_token is None:
            return None

        jwt_token = JWTAuthentication.get_the_token_from_header(jwt_token)  

        try:
            payload = jwt.decode(jwt_token, settings.SECRET_KEY, algorithms=['HS256'])
        except jwt.exceptions.InvalidSignatureError:
            raise AuthenticationFailed('Invalid signature')
        except:
            raise ParseError()
        print(payload)
        # Get the user from the database
        user_id = payload.get('user_identifier')
        print(user_id)
        if user_id is None:
            raise AuthenticationFailed('User identifier not found in JWT')

        try:
            print(payload)
            user = User.objects.get(id=user_id).first()
            return user,payload
        except User.DoesNotExist:
            return AuthenticationFailed("User Not Found")

        # Return the user and token payload
        
    def authenticate_header(self, request):
        return 'Bearer'

    @classmethod
    def create_jwt(cls, user):
        # Create the JWT payload
        payload = {
            'user_identifier': user.id,
            'exp': int((datetime.now() + timedelta(hours=72)).timestamp()),
            'iat': datetime.now().timestamp(),
            'mail': user.mail,
            'phone': user.phone
        }

        # Encode the JWT with your secret key
        jwt_token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')

        return jwt_token

    @classmethod
    def get_the_token_from_header(cls, token):
        token = token.replace('Bearer', '').replace(' ', '')  # clean the token
        return token