from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.feed, name='feed'),
    path('upload/', views.upload_post, name='upload'),
    path('like/<int:post_id>/', views.like_post, name='like'),
    path('comment/<int:post_id>/', views.comment_post, name='comment'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', LogoutView.as_view(template_name='logged_out.html'), name='logout'),
    path('user/<str:username>/', views.user_profile, name='user_profile'),
    path('signup/', views.signup_view, name='signup'),
]