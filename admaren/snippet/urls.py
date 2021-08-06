from .views import *
from django.urls import path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="DRF Class API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@me.local"),
      license=openapi.License(name="test License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)



urlpatterns = [
    path('', apiOverview, name='api-overview'),
    path('api/tags_list/', TagsList.as_view(), name='tags-list'),
    path('api/snippet_list/', SnippetList.as_view(), name='snippet-list'),
    path('api/snippet_detail/<str:pk>/', SnippetDetail.as_view(), name='snippet-detail'),

    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]