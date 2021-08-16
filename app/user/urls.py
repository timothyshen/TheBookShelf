from django.urls import path
from .views import CreateAccount, AllUsers, ReaderLoginView, AuthorLoginView

app_name = 'users'
urlpatterns = [
    path('create/', CreateAccount.as_view(), name="create_user"),
    path('all/', AllUsers.as_view(), name="all"),
    path('currentUser/', ReaderLoginView.as_view(), name="reader"),
    path('authorUser/', AuthorLoginView.as_view(), name="author"),
]
