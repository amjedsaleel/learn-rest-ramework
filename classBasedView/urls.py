from django.urls import path

from . import views

urlpatterns = [
    path('', views.SnippetList.as_view()),
    path('detail/<int:pk>', views.Detail.as_view())

]
