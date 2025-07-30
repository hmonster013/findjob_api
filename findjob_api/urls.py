"""
URL configuration for findjob_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf import settings
from drf_yasg import openapi
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from findjob_api.admin import custom_admin_site

schema_view = get_schema_view(
    openapi.Info(
        title="Find Job API",
        default_version="V1",
        description="API documentation using Swagger",
        terms_of_service="https://yourdomain.com/terms/",
        contact=openapi.Contact(email="tranphuhuyit@gmail.com"),
        license=openapi.License(name="MIT License")
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    # Admin
    path('admin/', custom_admin_site.urls),
    # Swagger
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    re_path(r"^swagger(?P<format>\.json|\.yaml)$", schema_view.without_ui(cache_timeout=0), name="schema-json"),
    # OAuth2
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    # Base
    path('api/', include(
        [
            path('common/', include('common.urls')),    
            path('auth/', include('authentication.urls')),
            path('info/', include('info.urls')),
            path('job/', include('job.urls')),
            path('findjob/', include('findjob.urls')),
            path('chatbot/', include('chatbot.urls')),
        ]
    ))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


