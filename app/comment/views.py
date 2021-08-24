from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from comment.models import Comment
from comment.pagination import PostPageNumberPagination
from comment.serializers import CommentSerializer


class CommentPublicView(ListCreateAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    search_fields = ['content', 'user__first_name']
    pagination_class = PostPageNumberPagination  # PageNumberPagination

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CommentDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.filter(id__gte=0)
    serializer_class = CommentSerializer

    # permission_classes = [IsOwnerOrReadOnly]

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
