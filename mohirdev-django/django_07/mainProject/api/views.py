from rest_framework.generics import ListAPIView
from application.models import Book
from .serializers import BookSerializer

# # Create your views here.
class BookListView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer