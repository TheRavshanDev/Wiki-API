from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from .models import Post
from user.models import Author
from .serializers import PostSerializer, AuthorSerializer
from rest_framework.response import Response
from rest_framework import status, filters

class AuthorView(APIView):
    filter_backends = [filters.OrderingFilter, filters.SearchFilter,]
    ordering_fields = ['name','age',]
    search_fields = ['name','username','age','proffession',]
    def get(self):
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        author = get_object_or_404(Author, id=pk)
        serializer = AuthorSerializer(author, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        author = get_object_or_404(Author, id=pk)
        author.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class PostView(APIView):
    filter_backends = [filters.SearchFilter,]
    search_fields = ['post_title','post_text','post_date',]
    def get(self):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        post = get_object_or_404(Post, id=pk)
        serializer = PostSerializer(post, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        post = get_object_or_404(Post, id=pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)