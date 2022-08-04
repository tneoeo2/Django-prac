"""dj003 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, re_path, include
from django.conf import settings
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
  openapi.Info(
    title="Swagger Study API",
    default_version = "v1",
    description="Swagger 공부용 API",
    terms_of_service="https://www.google.com/policies/terms/",
    contact = openapi.Contact(name="test", email="test@test.com"),
    license=openapi.License(name="Test License"),
  ),
  public = True,
  permission_classes=(permissions.AllowAny,),
  
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mysite.urls'))
]

#DEGUG일시, swagger 문서가 보이게 해주는 설정
#url 설정도 가능(ex)debug일때만 작동가능한 api 설정 가능)
if settings.DEBUG:
    urlpatterns += [
        re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name="schema-json"),
        re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
        re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),    ]



