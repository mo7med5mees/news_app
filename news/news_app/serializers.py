from rest_framework import serializers
from .models import Article, Category, Comment, Like

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class ArticleSerializer(serializers.ModelSerializer):
    category_id = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), source='category', write_only=True)  # Accept category_id directly
    category_name = serializers.CharField(source='category.name', read_only=True)  # Display category name in the response
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    author_username = serializers.CharField(source='author.username', read_only=True)

    class Meta:
        model = Article
        fields = ['id', 'title', 'content', 'author', 'author_username', 'category_id', 'category_name', 'created_at']
        read_only_fields = ['id', 'created_at']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = "__all__"