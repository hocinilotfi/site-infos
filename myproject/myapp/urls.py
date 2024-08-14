from django.urls import path
from .views import (
    UserRegisterView,
    UserDetailView,
    PostListView,
    PostDetailView,
    CommentCreateView,
)
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    # Authentification et gestion des utilisateurs
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('me/', UserDetailView.as_view(), name='user_detail'),

    # Gestion des posts
    path('posts/', PostListView.as_view(), name='post_list'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post_detail'),

    # Gestion des commentaires
    path('posts/<int:pk>/comments/', CommentCreateView.as_view(), name='comment_create'),
]
