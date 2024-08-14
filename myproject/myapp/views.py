from rest_framework import generics, permissions
from django.contrib.auth import get_user_model
from .models import Post, Comment
from .serializers import UserRegisterSerializer, UserDetailSerializer, PostSerializer, CommentSerializer
from rest_framework_simplejwt.tokens import RefreshToken

# Utilisateur personnalisé
User = get_user_model()

# Vue pour l'inscription d'un utilisateur
class UserRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = [permissions.AllowAny]

# Vue pour les détails de l'utilisateur (affichage et modification)
class UserDetailView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    permission_classes = [permissions.IsAuthenticated]
    # permission_classes = [permissions.AllowAny]

    def get_object(self):
        return self.request.user

# Vue pour la liste des posts
class PostListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.AllowAny]

# Vue pour les détails d'un post
class PostDetailView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.AllowAny]

# Vue pour la création d'un commentaire
class CommentCreateView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]
    # permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        post = Post.objects.get(pk=self.kwargs['pk'])
        serializer.save(user=self.request.user, post=post)
