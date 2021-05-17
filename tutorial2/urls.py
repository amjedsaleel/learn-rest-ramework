from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    path('snippet', views.snippet_list, name='snippet'),
    path('snippet-detail/<int:pk>', views.snippet_detail, name='snippet-detail')
]

