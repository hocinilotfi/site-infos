from django.db import models
from django.contrib.auth.models import AbstractUser

# Modèle d'utilisateur personnalisé
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True, blank=False, null=False) 
    job = models.CharField(max_length=255, blank=True, null=True)
    about_me = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.username

# Modèle pour les posts
class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# Modèle pour les commentaires
class Comment(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.user.username} on {self.post.title}'
