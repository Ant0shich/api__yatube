from rest_framework import serializers
from rest_framework.relations import SlugRelatedField


from posts.models import Comment, Post, Group, Follow


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = '__all__'
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(read_only=True,
                              slug_field='username')
    post = SlugRelatedField(read_only=True,
                            slug_field='id')

    class Meta:
        fields = ('id', 'author', 'text', 'created', 'post')
        model = Comment


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Group


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        slug_field="username",
        read_only=True)
    following = SlugRelatedField(slug_field='username',
                                 read_only=True)

    class Meta:
        fields = ('user', 'following')
        model = Follow
