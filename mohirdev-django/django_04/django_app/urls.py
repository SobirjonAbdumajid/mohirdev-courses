from django.urls import path
from .views import HomepageView, AboutPageView

urlpatterns = [
    path('', HomepageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about')
]