"""TheBookshelf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.documentation import include_docs_urls
from rest_framework.schemas import get_schema_view
from TheBookshelf.views import IndexTemplateView
# DRF YASG
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Djoser API",
        default_version="v1",
        description="REST implementation of Django authentication system. djoser library provides a set of Django Rest Framework views to handle basic actions such as registration, login, logout, password reset and account activation. It works with custom user model.",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('user.urls')),
    path('api/v1/', include('product.urls')),
    path('api/v1/', include('payment.urls')),
    path('api/v1/', include('bookcase.urls')),
    path('api/v1/', include('bookitem.urls')),
    path('api/v1/', include('comment.urls')),
    path('project/docs/', include_docs_urls(title='BlogAPI')),
    path(
        r"api/v1/docs/",
        schema_view.with_ui('redoc', cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path('api/auth/', include('rest_framework.urls')),
    path('api-auth/', include('drf_social_oauth2.urls', namespace='drf')),
]
