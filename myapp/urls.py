from django.contrib import admin
from django.urls import path,include
from. import views

urlpatterns = [
    path('index/',views.home,name='index'),
    path('',views.logins,name='sigin'),
    path('signin/',views.signupp,name='signup'),
    path('logout/',views.logoutt,name='logout'),
    path('post/',views.add_post,name='add-post'),
    path('profile/',views.profiles,name='profile'),
    path('edit/',views.profile_edit,name='profile-edit'),
    path('like/<int:pk>',views.likes,name='like'),
    path('dislike/<int:pk>',views.dislikes,name='dislike'),
    path('viewprofile/<int:pk>',views.view_profiles,name='view-profile'),
    path('follower/<int:pk>',views.following,name='followings'),
    path('unfollow/<int:pk>',views.un_follow,name='un-follow'),
    path('followings/<int:pk>',views.followings,name='followingss'),
    path('search/',views.searched,name='searc'),
    path('postdetail/<int:pk>',views.post_detail,name='post-detail'),
    path('friendlist/',views.view_friend,name='view-friend'),













]