from .models import Tags, Snippets
from rest_framework import serializers


class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = '__all__'


class SnippetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Snippets
        fields = '__all__'
