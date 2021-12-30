# Create your views here.
from django.contrib.auth.decorators import login_required
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from bookitem.models import Book
from comment.models import Comment
from comment.pagination import PostPageNumberPagination
from comment.serializers import CommentSerializer
from notifications.signals import notify  # 消息通知

from user.models import AuthUser


class CommentPublicView(ListCreateAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    search_fields = ['content', 'user__first_name']
    pagination_class = PostPageNumberPagination  # PageNumberPagination

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        self.cm_message_send()#评论通知
        self.like_msg_send()#点赞通知

    #Message send to user when someone put a comment./ 消息发送至用户当有用户进行评论
    def cm_message_send(self):
        data = self.request.data
        book = Book.objects.get(id=data['book'])
        user_name = AuthUser.objects.get(id=data['user'])
        if self.request.user != book.book_author:
            notify.send(self.request.user, recipient=book.book_author,
                        verb='你的名为<b>%s</b>的文章被<b>%s</b>评论了，<a href = "%s"> 前往查看 </a> ' % (
                            book.book_name, user_name.username, Comment.get_absolute_url))


    def like_msg_send(self):
        data = self.request.data
        book = Book.objects.get(id=data['book'])
        user_name = AuthUser.objects.get(id = data['user'])
        if 'likes' in data and data['likes'] == 1:
            notify.send(self.request.user, recipient=book.book_author,
                        verb='你的名为<b>%s</b>的文章被<b>%s</b>点赞了' % (
                            book.book_name, user_name.username))


class CommentDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.filter(id__gte=0)
    serializer_class = CommentSerializer

    # permission_classes = [IsOwnerOrReadOnly]

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
