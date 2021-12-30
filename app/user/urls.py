from django.urls import path
from .views import CreateAccount, AllUsers, ReaderLoginView, AuthorLoginView, UserDetailView

app_name = 'users'
urlpatterns = [
    path('createUser/', CreateAccount.as_view(), name="create_user"),
    path('all/', AllUsers.as_view(), name="all-users"),
    path('currentUser/', ReaderLoginView.as_view(), name="reader-details"),
    path('authorUser/', AuthorLoginView.as_view(), name="author-details"),
    path('user/<int:pk>/', UserDetailView.as_view(), name="user-details"),
]
