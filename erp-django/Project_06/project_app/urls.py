from django.urls import path
from .views import home, about

urlpatterns = [
    path('home/', home),
    path('about/', about)
]