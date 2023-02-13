
from django.urls import path, include
from .views import  PostsListView, PostDetailView
urlpatterns = [
    path('', PostsListView.as_view()),
    path('<pk>/', PostDetailView.as_view()),
]