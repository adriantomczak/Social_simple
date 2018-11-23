from django.urls import path
from .views import PostList, UserPosts, PostDetail, CreatePost, DeletePost

app_name = 'posts'

urlpatterns = [
    path('', PostList.as_view(), name='all'),
    path('new/', CreatePost.as_view(), name='create'),
    path('by/(<username>[-\w]+)/', UserPosts.as_view(), name='for_user'),
    path('by/(<username>[-\w]+)/(<pk>\d+)/', PostDetail.as_view(), name='single'),
    path('delete/(<pk>\d+)/', DeletePost.as_view(), name='delete')
]