from .views import *
from django.urls import path

urlpatterns = [
    path('', apiOverview, name='api-overview'),
    path('api/tags_list/', TagsList.as_view(), name='tags-list'),
    path('api/snippet_list/', SnippetList.as_view(), name='snippet-list'),
    path('api/snippet_detail/<str:pk>/', SnippetDetail.as_view(), name='snippet-detail'),

]