from django.urls import path
from .views import BookListCreateView, BookRetrieveUpdateDestroyView, StudentBookListView, AdminSignupView

urlpatterns = [
    path('books/', BookListCreateView.as_view(), name='book-list-create'),
    path('books/<int:pk>/', BookRetrieveUpdateDestroyView.as_view(), name='book-retrieve-update-destroy'),
    path('student/books/', StudentBookListView.as_view(), name='student-book-list'),
    path('signup/', AdminSignupView.as_view(), name='admin-signup'),
]