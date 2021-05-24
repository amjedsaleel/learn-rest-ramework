from django.shortcuts import render

# Rest framework
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView, RetrieveAPIView

# local Django
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from snippets.permissions import IsOwnerOrReadOnly


# Create your views here.


class SnippetList(CreateAPIView):
    serializer_class = SnippetSerializer

    # def get_queryset(self):
    #     return Snippet.objects.filter(pk=3)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class Detail(RetrieveUpdateDestroyAPIView):
    # lookup_url_kwarg = pk
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
