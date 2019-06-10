"""AppIDJWTSample URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import include, path
from django.conf.urls import url
from rest_framework import routers
from rest_framework_jwt.views import verify_jwt_token
from .jwtview import JWTView


router = routers.DefaultRouter()
router.register('jwt-verify', JWTView, basename="JWTView")

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api-token-verify/', verify_jwt_token),  #won't work because the authenticate_credentials method needs to be overridden
]
