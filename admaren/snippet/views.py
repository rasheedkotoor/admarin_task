from django.shortcuts import render
from .models import Snippets, Tags
from .serializers import SnippetSerializer, TagsSerializer
# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'Tags Create, List': '/api/tags_list/',
        'Snippet Create, List': '/api/snippet_list/',
        'Snippet Detail, Update, Delete': '/api/snippet_detail/<str:pk>/',
    }
    return Response(api_urls)


class TagsList(ListCreateAPIView):
    queryset = Tags.objects.all()
    serializer_class = TagsSerializer


class SnippetList(ListCreateAPIView):
    queryset = Snippets.objects.all()
    serializer_class = SnippetSerializer


class SnippetDetail(RetrieveUpdateDestroyAPIView):
    queryset = Snippets.objects.all()
    serializer_class = SnippetSerializer
