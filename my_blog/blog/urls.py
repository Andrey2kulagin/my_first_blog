
from django.urls import path, include
from .views import  PostsListView, PostDetailView
urlpatterns = [
    path('', PostsListView.as_view()),
    path('<pk>/s', PostDetailView.as_view()),
]