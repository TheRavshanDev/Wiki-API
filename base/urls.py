from django.urls import path
from .views import *


urlpatterns = [
    path('',AuthorView.as_view(), name='author'),
    path('<int:pk>/',AuthorView.as_view(), name='author-pk'),
    path('post/',PostView.as_view(), name='post'),
    path('post/<int:pk>/',PostView.as_view(), name='post-pk'),
]