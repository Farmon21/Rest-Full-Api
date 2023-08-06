from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import (BookListApiView,
                    book_list_view,
                    BookDetailApiView,
                    BookDeleteApiView,
                    BookUpdateApiView,
                    BookCreateApiView,
                    BookListCreateApiView,
                    BookUpdateDeleteApi,
                    BookViewSet,)

router = SimpleRouter()
router.register('books', BookViewSet, basename='books')

urlpatterns = [
    path('books/', BookListApiView.as_view()),
    path('books/create/', BookCreateApiView.as_view()),
    path('books-create/', BookListCreateApiView.as_view()),
    path('books_view/', book_list_view),
    path('books/<int:pk>/', BookDetailApiView.as_view()),
    path('books/<int:pk>/delete/', BookDeleteApiView.as_view()),
    path('books/<int:pk>/update/', BookUpdateApiView.as_view()),
    path('book-update-delete/<int:pk>/', BookUpdateDeleteApi.as_view()),
]

urlpatterns += router.urls
