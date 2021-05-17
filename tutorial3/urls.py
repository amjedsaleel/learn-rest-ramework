from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

# app_name = 'tutorial-3'

urlpatterns = [
    path('snippet', views.SnippetList.as_view(), name='tutorial-3-snippet'),
    path('snippet-detail/<int:pk>', views.SnippetDetail.as_view(), name='tutorial-3-snippet-detail')
]

