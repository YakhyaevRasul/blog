from django.urls import path
from .views import PostListView, PostCreateView, PostDetailUpdateDeleteApiView

app_name='posts'

urlpatterns = [
    path('list/', PostListView.as_view(), name='posts-list'),
    path('create/', PostCreateView.as_view(), name='post-create'),
    path('<int:pk>/', PostDetailUpdateDeleteApiView.as_view(),name='post-detail'),
]