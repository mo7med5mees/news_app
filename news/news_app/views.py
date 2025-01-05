from rest_framework.permissions import BasePermission, SAFE_METHODS, IsAuthenticated
from rest_framework import viewsets

from .models import Article, Category, Comment, Like
from .serializers import ArticleSerializer, CategorySerializer, CommentSerializer, LikeSerializer

class IsManagerOrReadOnly(BasePermission):
    """
    Custom permission: Only users in the 'Manager' group can modify articles.
    """
    def has_permission(self, request, view):
        # Allow safe methods (GET, HEAD, OPTIONS) for all users
        if request.method in SAFE_METHODS:
            return True
        
        # Allow only users in the Manager group to make changes
        return request.user.groups.filter(name="Manager").exists()
    


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsManagerOrReadOnly]

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsManagerOrReadOnly]


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [IsAuthenticated]
