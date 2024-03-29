from django.urls import path
from .views import PostListAPIView, PostDetailAPIView
#PostCreateAPIView)

app_name = 'api'
urlpatterns = [
    path('', PostListAPIView.as_view(), name='list'),
    #path('create/', PostCreateAPIView.as_view(), name='create'),
    path('<int:pk>/', PostDetailAPIView.as_view(), name='detail'),
]