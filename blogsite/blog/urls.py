from django.urls import path
from . import views

urlpatterns=[
    path("",views.home,name="home"),
    path("home/",views.home,name="home"),
    path("check/<str:username>/",views.check_accounts),
    path("registration/",views.create_ac,name="create_ac"),
    path("profile/",views.profile,name="profile"),
    path("login/",views.user_login,name="login"),
    path("logout/",views.user_logout,name="logout"),
    path("newblog/",views.new_blog,name="new_blog"),
    path("blogs/",views.blogs,name="blog"),
    path("forgetpassword",views.forget_password,name="forget_password"),
    path("blogs/<str:keywords>",views.blog_search,name="blog_serch"),
    
]