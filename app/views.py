from django.shortcuts import render
from api.serializers import PostSerializer
from posts.models import Post
from rest_framework.views import APIView, Response
from rest_framework import generics


# class PostListView(APIView):
#     def get(self,request):
#         posts = Post.objects.all()
#         serializer = PostSerializer(posts, many=True)
#         return Response(serializer.data)


class PostListAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


# class PostCreateAPIView(generics.CreateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

class PostDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


# class PostDeleteAPIView(generics.DestroyAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#
# class PostUpdateAPIView(generics.UpdateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
from django.shortcuts import render

# Create your views here.
