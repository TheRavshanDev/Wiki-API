from django.urls import path
from .views import *
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Wikipedia API",
      default_version='v1.0',
      description="",
      contact=openapi.Contact("Ravshanbek Madaminov <ravshanbekmadaminov68@gmail.com> <+998903036415>"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path('',AuthorView.as_view(), name='author'),
    path('<int:pk>/',AuthorView.as_view(), name='author-pk'),
    path('post/',PostView.as_view(), name='post'),
    path('post/<int:pk>/',PostView.as_view(), name='post-pk'),
    path('documentation/swagger/',schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('documentation/redoc/',schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc-ui'),
]