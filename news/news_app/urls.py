from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ArticleViewSet, CategoryViewSet, CommentViewSet

router = DefaultRouter()
router.register(r'articles', ArticleViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('api/', include(router.urls)),

# Djoser endpoints
    path('api/auth/', include('djoser.urls')),  
    path('api/auth/', include('djoser.urls.authtoken')), 
]