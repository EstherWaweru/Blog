from blog import views
from blog.views import AboutView,PostListView,PostDetailView,CreatePostView,UpdatePostView,DeletePostView,DraftListView
from django.urls import path

urlpatterns = [
  path('',PostListView.as_view(),name='post_list'),
  path('post/<int:pk>/',PostDetailView.as_view(),name='post_detail'),
  path('post/new/',CreatePostView.as_view(),name='post_new'),
  path('post/<int:pk>/edit/',UpdatePostView.as_view(),name='post_edit'),
  path('post/<int:pk>/remove/',DeletePostView.as_view(),name='post_remove'),
  path('drafts/',DraftListView.as_view(),name='post_draft_list'),
  path('about/', AboutView.as_view(), name='about'),
  path('post/<int:pk>/comment/',views.add_comment_to_post,name='add_comment_to_post'),
  path('comment/<int:pk>/approve/',views.comment_approve,name='comment_approve'),
  path('comment/<int:pk>/remove/',views.comment_remove,name='comment_remove'),
  path('post/<int:pk>/publish/',views.post_publish,name='post_publish'),


 ]
