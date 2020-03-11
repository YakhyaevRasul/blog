from rest_framework import mixins
from .models import Post
from rest_framework import generics
from .serializers import PostSerializer, PostCreateSerializer, PostDetailSerialzier
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAuthorOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.user == request.user

class PagePagination(PageNumberPagination):
    page_size = 2

class PostListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, ]
    pagination_class = PagePagination

class PostCreateView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateSerializer
    permission_classes = [IsAdminUser, ]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PostDetailUpdateDeleteApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerialzier
    permission_classes = [IsAuthorOrReadOnly, ]
