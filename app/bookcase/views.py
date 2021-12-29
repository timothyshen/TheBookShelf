# Create your views here.
from rest_framework.generics import CreateAPIView, ListCreateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated

from .serializer import *


# Create your views here.
class BookcaseView(ListCreateAPIView):
    permission_classes = [IsAuthenticated, ]
    serializer_class = BookCaseSerializer

    def get_queryset(self):
        return Bookcase.objects.filter(user_id=self.request.user)


class BookcaseDeleteView(DestroyAPIView):
    permission_classes = [IsAuthenticated, ]
    serializers_class = BookCaseSerializer

    def get_queryset(self):
        return Bookcase.objects.filter(user_id=self.request.user)


class BookMarkView(CreateAPIView):
    serializer_class = BookMarkSerializer
    queryset = BookMark.objects.all()
    permission_classes = [IsAuthenticated, ]
