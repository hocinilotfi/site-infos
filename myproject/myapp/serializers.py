from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Post, Comment

# Modèle utilisateur personnalisé
User = get_user_model()

# Sérializer pour l'inscription d'un utilisateur
class UserRegisterSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'job', 'about_me')

    def validate(self, data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError("Les mots de passe ne correspondent pas.")
        return data

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            email=validated_data['email'],
            job=validated_data.get('job', ''),
            about_me=validated_data.get('about_me', '')
        )
        user.set_password(validated_data['password1'])
        user.save()
        return user

# Sérializer pour afficher et modifier les détails de l'utilisateur
class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'job', 'about_me')



# Sérializer pour les commentaires
class CommentSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('user', 'post')

# Sérialiseur pour les posts avec les commentaires imbriqués
class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = '__all__'