from django.urls import path
# from .views import ListAPIView
from .views import BookListView
urlpatterns = [
    path('', BookListView.as_view()),
]